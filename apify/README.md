# apify

## Facebook

```bash
# photos
dataset_facebook-photos-scraper_2025-12-11_04-18-53-041.json | jq -r .[].image > urls.txt

# reels
cat dataset_facebook-reels-scraper_2025-12-11_05-23-07-115.json | jq -r .[].playback_video.videoDeliveryLegacyFields.browser_native_hd_url > urls.txt
```
