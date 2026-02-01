package main

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"sync"

	_ "github.com/joho/godotenv/autoload"
	"github.com/schollz/progressbar/v3"
)

var tag = "h/recipes"

func addBookmark(url string, wg *sync.WaitGroup, bar *progressbar.ProgressBar) {
	defer wg.Done()

	jsonData := []byte(fmt.Sprintf(`{
  "url": "%s",
  "is_archived": false,
  "unread": false,
  "shared": false,
  "tag_names": [
   "%s"
  ]
}`, url, tag))

	req, err := http.NewRequest("POST", fmt.Sprintf("%s/api/bookmarks/", os.Getenv("LINKDING_ENDPOINT")), bytes.NewBuffer(jsonData))
	if err != nil {
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", fmt.Sprintf("Token %s", os.Getenv("LINKDING_TOKEN")))

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
	}
	defer resp.Body.Close()

	bar.Add(1)
}

func main() {
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

	for _, url := range urls {
		wg.Add(1)
		go addBookmark(url, &wg, bar)
	}

	wg.Wait()
}
