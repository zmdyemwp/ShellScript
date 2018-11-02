if [%1] equ [] goto:NO_SN

    fastboot -s %1 erase userdata
    goto:eof

:NO_SN
    fastboot erase userdata
    goto:eof