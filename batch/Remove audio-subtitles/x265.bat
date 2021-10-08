for %%i in (*.mkv) do mkvmerge -o new_folder/"%%i" --c:v libx265 --preset slow --x264-params lossless=1
