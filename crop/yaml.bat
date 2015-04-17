@echo off
set crop=crop.exe

set src=crop.lst
set tgt=layout_coord.yaml
echo =^> Generate a YAML file (%tgt%) of screens with coordinate layouts.
%crop% yaml -o%tgt% %src%

pause

