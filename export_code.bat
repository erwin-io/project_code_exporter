@echo off
setlocal

set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%export_project.py

echo.
echo ================================
echo Smart Project Code Exporter
echo TXT Only - No External Libraries
echo ================================
echo.

set /p PROJECT_DIR=Enter project folder path: 

echo.
echo Auto-detecting project type...
echo.

python "%PYTHON_SCRIPT%" "%PROJECT_DIR%"

echo.
pause