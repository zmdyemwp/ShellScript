@ECHO OFF

IF [%1]==[] GOTO:NO_SN ELSE GOTO:DO_SN

REM adb -s %s shell am broadcast -a android.intent.action.FACTORY_RESET --receiver-include-background
:NO_SN
    adb shell am broadcast -a android.intent.action.FACTORY_RESET --receiver-include-background
    GOTO:EOF

:DO_SN
    adb -s %1 shell am broadcast -a android.intent.action.FACTORY_RESET --receiver-include-background
    GOTO:EOF