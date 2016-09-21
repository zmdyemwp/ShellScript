@echo off
IF "%1" NEQ "" (
	IF "%2" NEQ "" (
		Mkyreporter_v3.1.jar --errinf -m sys -o %1 -v %2
	) ELSE (
		Mkyreporter_v3.1.jar --errinf -m sys -o %1
	)
	echo Add report at %1
) ELSE (
	echo Please input Monkey folder.
)