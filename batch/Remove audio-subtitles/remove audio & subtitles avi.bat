for %%i in (*.avi) do mkvmerge -o new_folder/"%%i" --atracks 2 --no-subtitles "%%i"
