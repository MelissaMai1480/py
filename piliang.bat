@echo off
setlocal enabledelayedexpansion
echo "请输入要删除哪个字符串前的内容"
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