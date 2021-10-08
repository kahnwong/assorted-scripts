for %%a in ("*.mkv") do ffmpeg -i "%%a" -c:v copy -c:a aac -b:a 128k  -c:s mov_text "D:\z-comics_temp_to_device\videos\%%~na.mp4"
pause
