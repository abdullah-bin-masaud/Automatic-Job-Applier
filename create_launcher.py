from pathlib import Path

bat_content = """@echo off
title Abdullah Bin Masaud - Automated Job Application Engine
cd /d "C:\\Users\\Lenovo\\Desktop\\Projects\\Automated-Job-Applier"
py main.py
pause
"""

desktop_bat = Path(r"C:\Users\Lenovo\Desktop\RUN_JOB_APPLIER.bat")
desktop_bat.write_text(bat_content, encoding="utf-8")
print(f"Created launcher on Desktop: {desktop_bat}")
