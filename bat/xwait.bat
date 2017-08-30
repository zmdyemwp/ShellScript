@ECHO OFF
ECHO Wait for %1% seconds
PING 127.0.0.1 -n %1 > nul || PING ::1 -n %1 > nul