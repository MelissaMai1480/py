@echo off
setlocal enabledelayedexpansion
echo "������Ҫɾ���ĸ��ַ���ǰ������"
set /p str=
setlocal enabledelayedexpansion
FOR %%F IN (*%str%*.*) DO (
SET FileName=%%~nF
SET FileName=!FileName:*%str%=!
SET FileName=!FileName!%%~xF
ECHO !FileName!
RENAME %%F !FileName!
)
ENDLOCAL