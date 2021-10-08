for %%A IN (*.*) DO ffmpeg -i "%%A"   -vn -acodec copy "%%A.m4a"
