for %%a in ("*.*") do ffmpeg -i "%%a" -c:v libx265 -preset medium -crf 28 -c:a copy "newfiles\%%~na.mp4"
pause
