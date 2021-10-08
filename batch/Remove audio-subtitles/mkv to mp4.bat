mkdir "newfiles"
for %%a in ("C:\Users\Khan\Desktop\New folder\new_folder\*.mkv") do ffmpeg -i "%%a" -vcodec copy -acodec copy "C:\Users\Khan\Desktop\%%~na.mp4"
pause
