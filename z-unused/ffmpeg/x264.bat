for %%a in ("*.mkv") do ffmpeg -i "%%a" -c:v libx264 -preset medium -crf 28 -c:a copy "newfiles\%%~na.mkv"
pause
