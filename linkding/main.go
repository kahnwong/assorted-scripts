package main

import (
	"bytes"
	"fmt"
	"net/http"
	"os"

	_ "github.com/joho/godotenv/autoload"
	"github.com/schollz/progressbar/v3"
)

func addBookmark(url string) {
	jsonData := []byte(fmt.Sprintf(`{
  "url": "%s",
  "is_archived": false,
  "unread": false,
  "shared": false,
  "tag_names": [
    "d/books"
  ]
}`, url))

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

	//body, err := io.ReadAll(resp.Body)
	//if err != nil {
	//}
	//fmt.Println(string(body))
}

func main() {
	urls := []string{
		"https://news.ycombinator.com/item?id=42218828",
	}

	bar := progressbar.Default(int64(len(urls)))
	for _, url := range urls {
		addBookmark(url)
		bar.Add(1)
	}
}
