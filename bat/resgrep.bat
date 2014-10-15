@ echo:
@ echo RESGREP: %1%
@ echo ---------------------------------------------------------------------
@ echo        [*.xml]
@ findstr /i /s /n /a:0d /c:%1% *.xml*
@ echo: