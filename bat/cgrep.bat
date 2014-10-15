@ echo:
@ echo CGREP: %1%
@ echo ---------------------------------------------------------------------
@ echo        [*.h]
@ findstr /i /s /n /a:0d /c:%1% *.h*
@ echo:
@ echo        [*.c/*.cpp]
@ findstr /i /s /n /a:0d /c:%1% *.c*