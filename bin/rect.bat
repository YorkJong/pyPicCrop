@echo off
set crop=crop.exe

set src=crop.lst
set screen_dir=screen
set out_dir=out
echo =^> Mark out rectangles from a crop-list file.
%crop% rect -s%screen_dir% -o%out_dir% %src%

pause
