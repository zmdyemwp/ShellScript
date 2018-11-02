@ECHO OFF

FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (ECHO %%I&&adb -s %%I shell reboot -p)