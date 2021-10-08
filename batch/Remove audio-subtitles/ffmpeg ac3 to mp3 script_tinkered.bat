
mkdir Gear
for %%F in (*.mkv) do ( ffmpeg -i "%%F" -c:v copy -c:a mp3 -b:a 320k "Gear/%%F" )
