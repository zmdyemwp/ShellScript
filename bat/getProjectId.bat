@REM
@REM        Mapping Project Name and the Vendor ID for fastboot command
@REM
@REM

@   IF %1 == v06 SET VAR = 0x27f1 & GOTO :END

@   IF %1 == V06 SET VAR = 0x27f1 & GOTO :END

@   IF %1 == fh2 SET VAR = 0x489 & GOTO :END

@   IF %1 == FH2 SET VAR = 0x489 & GOTO :END


:END
@   ENDLOCAL
@   SET %~2 = VAR
