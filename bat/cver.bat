@echo off
if [%1] equ [] goto:no_sn

adb -s %1 shell cat /system/build_id
goto:eof

:no_sn
adb shell cat /system/build_id
goto:eof