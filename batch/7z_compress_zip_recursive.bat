FOR /R /D %%F in (*) do (
    7z a "%%F.zip" "%%F\"
    RMDIR /s /q "%%F"
    ren *.zip *.cbz
)
