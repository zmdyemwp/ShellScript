@ECHO OFF

logcheck.py . > analysis.ana
crash_counter.py . >> analysis.ana

analysis.ana