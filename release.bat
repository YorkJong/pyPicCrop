@echo off

set bin_dir=crop-bin
set target=crop

if not exist %bin_dir% (
    md %bin_dir%
)

echo =^> Generating the executable file
call build.bat %target% SkipPause
move %target%.exe %bin_dir%

echo =^> Moving the test files
xcopy %target%\tests\screen %bin_dir%\screen\
copy %target%\tests\crop.lst %bin_dir%
copy %target%\tests\rect.bat %bin_dir%
copy %target%\tests\crop.bat %bin_dir%
copy %target%\tests\yaml.bat %bin_dir%

pause
