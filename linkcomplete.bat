@ECHO OFF
set TORRENT_ID=%1
set TORRENT_NAME=%2
set SAVE_DIR=%3

pushd %SAVE_DIR%
cd ..
set TEMP_DIR=%cd%

if exist %TORRENT_NAME%\ (
    set DEST_DIR=%TEMP_DIR%\#temp\%TORRENT_NAME%
    mkdir %DEST_DIR%
    pushd %SAVE_DIR%\%TORRENT_NAME%
    forfiles /C "cmd /c mklink /h %DEST_DIR%\@file @file"
) else (
    set DEST_DIR=%TEMP_DIR%\#temp\
    mklink /h %DEST_DIR%\%TORRENT_NAME% %SAVE_DIR%\%TORRENT_NAME%
)


