@ECHO OFF
IF [%1] EQU [] (
    ECHO FASTBOOT REBOOT
    fastboot reboot
) ELSE (
    ECHO FASTBOOT REBOOT %1
    fastboot -s %1 reboot
)
