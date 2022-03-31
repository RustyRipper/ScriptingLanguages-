ECHO OFF

SET LIST= %*


ECHO Wprowadz tekst:
java KodPowrotu %LIST%

SET /A KOD=%ERRORLEVEL%
SET /A COUNTER = 1

setlocal ENABLEDELAYEDEXPANSION

IF %KOD% EQU 0 (
ECHO Brak wystapien parametru
GOTO end
)

FOR %%A in (%LIST%) DO (

IF !COUNTER! EQU %KOD% (ECHO Program uznal ze najczesciej wystepuje parametr { %%A })

set /a COUNTER +=1
)
:end
endlocal