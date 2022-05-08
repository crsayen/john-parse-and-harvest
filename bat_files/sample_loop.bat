cd c:\work\pyharvest
:loop
py list_drivers.py
py harvest.py
timeout /T 15 /NOBREAK
goto loop