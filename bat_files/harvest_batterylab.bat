cd M:/pyharvest
:loop
call "C:/Users/teststand/Anaconda3/Scripts/activate.bat"
"C:/Users/teststand/Anaconda3/python.exe" "M:/pyharvest/harvest_batterylab.py"
timeout /T 120 /NOBREAK
goto loop
