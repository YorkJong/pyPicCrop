@echo off
set crop=..\crop\crop.py

set src=crop.lst
set screen_dir=screen
set out_dir=out
echo =^> Crop out pictures from screen pictures.
%crop% crop -s%screen_dir% -o%out_dir% %src%

set src=crop.lst
set screen_dir=screen
set out_dir=out
echo =^> Mark out rectangles from a crop-list file.
%crop% rect -s%screen_dir% -o%out_dir% %src%

set src=crop.lst
set tgt=layout_coord.yaml
echo =^> Generate a YAML file (%tgt%) of screens with coordinate layouts.
%crop% yaml -o%tgt% %src%

pause
