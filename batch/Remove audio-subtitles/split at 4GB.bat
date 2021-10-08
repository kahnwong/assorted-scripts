for %%i in (*.mkv) do mkvmerge -o new_folder/"%%i" --split size:100M "%%i"
