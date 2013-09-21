@ECHO OFF
set TORRENT_ID = %1
set TORRENT_NAME = %2
set SAVE_DIR = %3

pushd %SAVE_DIR%
cd ..
set TEMP_DIR = %cd%
popd

mklink /h %TEMP_DIR% %SAVE_DIR%\%TORRENT_NAME%
