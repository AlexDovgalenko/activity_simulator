@echo off
echo Starting Test Monitor Script...
echo Press `SHIFT+ESC` key to stop the script when finished

:: Change to the directory where your script is located
cd /d "<Path to project folder>"

:: Activate virtual environment
call venv\Scripts\activate.bat

uv run src\simulator.py

:: Deactivate virtual environment
deactivate

:: If there was an error, pause so you can see it
if %ERRORLEVEL% NEQ 0 (
    echo An error occurred while running the script.
    pause
)