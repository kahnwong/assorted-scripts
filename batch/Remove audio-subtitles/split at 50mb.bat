for %%i in (DIR\*.mkv) do mkvmerge -o C:\Users\Khan\Desktop\"%%i" --split size:50m "%%i"
