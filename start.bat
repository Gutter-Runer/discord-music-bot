@echo off
cd /d "%~dp0"

if not exist .venv\Scripts\python.exe (
  py -m venv .venv
  if errorlevel 1 python -m venv .venv
)

echo Updating yt-dlp (helps when YouTube breaks)...
.venv\Scripts\python.exe -m pip install -U yt-dlp
.venv\Scripts\python.exe -m pip install -r requirements.txt
echo Starting bot. Leave this window open. Ctrl+C to stop.
.venv\Scripts\python.exe bot.py
pause
