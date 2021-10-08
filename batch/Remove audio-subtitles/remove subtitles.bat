# assume input.mkv has 3 subtitle tracks
# remove subtitle track 2 (copy 1&3) from input.mkv & save to output.mkv
mkvmerge -o output.mkv --subtitle-tracks 1,3 input.mkv

# remove all subtitles (copy none)
mkvmerge -o output.mkv --no-subtitles input.mkv
