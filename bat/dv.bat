@ECHO OFF

if [%1] == [] GOTO:NO_SN

adb -s %1 disable-verity
PAUSE
adb -s %1 reboot

GOTO:EOF

:NO_SN
adb disable-verity
PAUSE
adb reboot

GOTO:EOF