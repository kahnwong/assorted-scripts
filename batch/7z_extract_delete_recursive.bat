FOR /R %%F in (*.cbz *.cbr) do (
    7z e "%%~pnxF" -o"%%~pnF" *.* -r
    del "%%~pnxF"
)
