@ set rootpath=LINUX\android

:begin

@cd | findstr "LINUX"
@ if 0 == %errorlevel% cd..
@ if 1 == %errorlevel% goto root

@ goto begin

:root
@ cd %rootpath%

:end