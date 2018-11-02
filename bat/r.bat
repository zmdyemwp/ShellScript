@ECHO OFF
adb kill-server


ECHO ENABLE ALL PORT
REM FOR %%J in (C D E F G H I J K L M N O P Q R S T U V W X Y Z A B) DO @(
FOR %%J in (C D E F G H I J K L M) DO @(
"ScsiCommandLine.exe" %%J SC_ENABLE_ALL_PORT
REM "E:\E1M_MKY\ScsiCommandLine.exe" %%J SC_ENABLE_ALL_PORT
)

REM CALL:WAIT 5
PAUSE
REM adb kill-server
adb devices


REM ECHO SWITCH PORT
REM FOR %%J in (C D E F G H I J K L M) DO @(
REM "ScsiCommandLine.exe" %%J SC_SWITCH_PORT_1
REM )


ECHO SWITCH ROOT
FOR %%J in (C D E F G H I J K L M) DO @(
"ScsiCommandLine.exe" %%J SC_SWITCH_ROOT
REM "E:\E1M_MKY\ScsiCommandLine.exe" %%J SC_SWITCH_ROOT
)


PAUSE


ECHO ADB ROOT
FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (adb -s %%I root)

PAUSE

ECHO ADB REMOUNT
FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (adb -s %%I remount)


GOTO:EOF

:WAIT
    ECHO Wait for %1 seconds
    @PING 127.0.0.1 -n %1 > nul || @PING ::1 -n %1 > nul
    GOTO:EOF