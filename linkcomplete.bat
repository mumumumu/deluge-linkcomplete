@ECHO OFF
SETLOCAL

set TORRENT_ID=%1
set TORRENT_NAME=%2
set SAVE_DIR=%3

pushd %SAVE_DIR%
cd ..
set TEMP_DIR=%cd%
set DEST_DIR=%TEMP_DIR%\#temp

if exist %SAVE_DIR%\%TORRENT_NAME%\ (
    if not exist %DEST_DIR%\%TORRENT_NAME% mkdir %DEST_DIR%\%TORRENT_NAME%
    pushd %SAVE_DIR%\%TORRENT_NAME%
    forfiles /C "cmd /c mklink /h %DEST_DIR%\%TORRENT_NAME%\@file @file"
) else (
    if not exist %DEST_DIR% mkdir %DEST_DIR%
    mklink /h %DEST_DIR%\%TORRENT_NAME% %SAVE_DIR%\%TORRENT_NAME%
)

pushd %SAVE_DIR%

ENDLOCAL
