@ECHO OFF

adb -s %1 pull /data/MKY_LOG/mky_event_123.txt %1.txt