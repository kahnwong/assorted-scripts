package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"

	wallabago "github.com/Strubbl/wallabago/v9"
	_ "github.com/joho/godotenv/autoload"
	"github.com/schollz/progressbar/v3"
)

// might need to re-run to make sure no requests are dropped due to sqlite backend

var tag = "" // CHANGE ME

func postEntry(url, title, tags string, starred, archive int) (int, error) {
	postData := map[string]string{
		"url":     url,
		"title":   title,
		"tags":    tags,
		"starred": strconv.Itoa(starred),
		"archive": strconv.Itoa(archive),
	}
	postDataJSON, err := json.Marshal(postData)
	if err != nil {
		return 0, err
	}

	req, err := http.NewRequest("POST", wallabago.LibConfig.WallabagURL+"/api/entries.json", strings.NewReader(string(postDataJSON)))
	if err != nil {
		return 0, err
	}

	authString, err := wallabago.GetAuthTokenHeader()
	if err != nil {
		return 0, err
	}

	req.Header.Add("Authorization", authString)
	req.Header.Add("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return 0, err
	}
	defer resp.Body.Close()

	_, err = io.Copy(io.Discard, resp.Body)
	return resp.StatusCode, err
}

func writeFailedURL(failedFile *os.File, failedMu *sync.Mutex, url string) {
	failedMu.Lock()
	defer failedMu.Unlock()

	if _, err := fmt.Fprintln(failedFile, url); err != nil {
		log.Printf("Failed to write %s to urls-failed.txt: %v", url, err)
	}
}

func addBookmark(url string, wg *sync.WaitGroup, bar *progressbar.ProgressBar, failedFile *os.File, failedMu *sync.Mutex) {
	defer wg.Done()

	statusCode, err := postEntry(url, "", tag, 0, 0)
	if err != nil {
		log.Printf("Failed to add %s: %v", url, err)
		writeFailedURL(failedFile, failedMu, url)
	} else if statusCode != http.StatusOK {
		log.Printf("Failed to add %s: status code %d", url, statusCode)
		writeFailedURL(failedFile, failedMu, url)
	}

	if err := bar.Add(1); err != nil {
		log.Printf("Failed to update progress bar: %v", err)
	}
}

func requiredEnv(key string) string {
	value := os.Getenv(key)
	if value == "" {
		log.Fatalf("%s is required", key)
	}

	return value
}

func main() {
	wallabago.SetConfig(wallabago.NewWallabagConfig(
		requiredEnv("WALLABAG_URL"),
		requiredEnv("WALLABAG_CLIENT_ID"),
		requiredEnv("WALLABAG_CLIENT_SECRET"),
		requiredEnv("WALLABAG_USERNAME"),
		requiredEnv("WALLABAG_PASSWORD"),
	))

	// Read URLs from file
	file, err := os.Open("urls.txt")
	if err != nil {
		log.Fatalf("Failed to open urls.txt: %v", err)
	}
	defer file.Close()

	var urls []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			urls = append(urls, line)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	if len(urls) == 0 {
		log.Fatal("No URLs found in urls.txt")
	}

	failedFile, err := os.Create("urls-failed.txt")
	if err != nil {
		log.Fatalf("Failed to create urls-failed.txt: %v", err)
	}
	defer failedFile.Close()

	var wg sync.WaitGroup
	var failedMu sync.Mutex
	bar := progressbar.Default(int64(len(urls)))

	// Limit concurrent goroutines
	semaphore := make(chan struct{}, 4)

	for _, url := range urls {
		wg.Add(1)
		semaphore <- struct{}{} // Acquire semaphore
		go func(u string) {
			defer func() {
				<-semaphore // Release semaphore
			}()
			addBookmark(u, &wg, bar, failedFile, &failedMu)
		}(url)
	}

	wg.Wait()
}
