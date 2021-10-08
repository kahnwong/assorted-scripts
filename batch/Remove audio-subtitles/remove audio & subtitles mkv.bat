for %%i in (*.mkv) do mkvmerge -o new_folder/"%%i" --atracks 2 --no-subtitles "%%i"
