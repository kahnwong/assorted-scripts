package main

import (
	"bufio"
	"log"
	"os"
	"strings"
	"sync"

	wallabago "github.com/Strubbl/wallabago/v9"
	_ "github.com/joho/godotenv/autoload"
	"github.com/schollz/progressbar/v3"
)

// might need to re-run to make sure no requests are dropped due to sqlite backend

var tag = "stationery" // CHANGE ME

func addBookmark(url string, wg *sync.WaitGroup, bar *progressbar.ProgressBar) {
	defer wg.Done()

	if err := wallabago.PostEntry(url, "", tag, 0, 0); err != nil {
		log.Printf("Failed to add %s: %v", url, err)
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

	var wg sync.WaitGroup
	bar := progressbar.Default(int64(len(urls)))

	// Limit concurrent goroutines to 2
	semaphore := make(chan struct{}, 4)

	for _, url := range urls {
		wg.Add(1)
		semaphore <- struct{}{} // Acquire semaphore
		go func(u string) {
			defer func() {
				<-semaphore // Release semaphore
			}()
			addBookmark(u, &wg, bar)
		}(url)
	}

	wg.Wait()
}
