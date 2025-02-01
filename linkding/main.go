package main

import (
	"bytes"
	"fmt"
	"io"
	"net/http"
	"os"

	_ "github.com/joho/godotenv/autoload"
)

func main() {
	urls := []string{
		"https://en.wikipedia.org/wiki/Carl_Hamilton_novels/",
	}

	for _, url := range urls {
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

		body, err := io.ReadAll(resp.Body)
		if err != nil {
		}
		fmt.Println(string(body))

	}
}
