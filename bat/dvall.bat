@ECHO ON
FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (adb -s %%I disable-verity)
FOR /F "tokens=1" %%I in ('adb devices') DO IF [%%I] NEQ [List] IF [%%I] NEQ [*] (adb -s %%I reboot)
