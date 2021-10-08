for %%i in (*.mkv) do mkvmerge -o new_folder/"%%i" --atracks 2  --subtitle-tracks 4 "%%i"
#--subtitle-tracks 1,3 input.mkv
