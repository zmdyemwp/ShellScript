
@if [%1] == [] goto :end

@if %1 == v06 goto :v06
@if %1 == fh2 goto :fh2
@goto :end

@REM =======================V06================================
:v06
    @set var=0x27f1
@goto :start

@REM =======================FH2================================    
:fh2
    @set var=0x489
@goto :start



@REM =======================START==============================    
:start
    @adb reboot bootloader & fastboot -i %var% flash system system.img
:end
@REM =======================END================================
