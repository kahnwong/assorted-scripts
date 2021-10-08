# ffmpeg

## ipod preset
ffmpeg -i "EPICA - Edge Of The Blade  (OFFICIAL VIDEO)-D_QLQHkj1XU.mp4" -vcodec libx264 -crf 23 -preset fast -profile:v baseline -level 3 -refs 6 -vf "scale=640:-1,pad=iw:480:0:(oh-ih)/2,format=yuv420p" -acodec copy output.mp4
