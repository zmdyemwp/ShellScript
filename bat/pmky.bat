@ECHO OFF
SET RESULT_FILE=%DIR%result.mky

logparser_plain_text.py . > %RESULT_FILE%
crashtimer_plain_text.py . >> %RESULT_FILE%