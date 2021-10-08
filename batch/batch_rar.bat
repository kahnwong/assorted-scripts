SET WINRAR="C:\Program Files\WinRAR"

    for /D %%f in (*) do (
        %WINRAR%\RAR.exe a -ep1 -r0 "%%~nxf.rar" "%%f"
    )
