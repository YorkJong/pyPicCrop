@echo off
set crop=crop.exe

set src=crop.lst
set screen_dir=screen
set out_dir=out
echo =^> Crop out pictures from screen pictures.
%crop% crop -s%screen_dir% -o%out_dir% %src%

pause
