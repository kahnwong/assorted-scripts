@echo off &setlocal enabledelayedexpansion
cd /d "%sourcefolder%"
set "line="
for %%a in (*.avi) do set line=!line! +"%%~a"
mkvmerge -o "output.mkv" %line:~2%
