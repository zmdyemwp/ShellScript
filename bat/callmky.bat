@ECHO OFF

IF [%1]==[] (GOTO:PS) ELSE (GOTO:PSA)


:PS
    ECHO Check Monkey Process:(PS)
    FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (ECHO Check Monkey @%%I&&adb -s %%I shell "ps | grep monkey"&&ECHO.)
    GOTO:GETUPTIME
:PSA
    ECHO Check Monkey Process:(PS -A)
    FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (ECHO %%I&&adb -s %%I shell "ps -A | grep monkey"&&ECHO.)
    GOTO:GETUPTIME

:GETUPTIME
ECHO.
ECHO.
ECHO Check Current Monkey Status:
FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (ECHO %%I&&adb -s %%I shell "uptime"&&adb -s %%I shell "tail -n 500 /data/MKY_LOG/mky_event_123.txt | grep 'Sending event'"&&adb -s %%I shell "cat /data/MKY_LOG/mky_event_123.txt | grep finished"&&ECHO.)



GOTO:EOF