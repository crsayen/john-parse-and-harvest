import pyodbc 

dlist = pyodbc.drivers()
for d in dlist:
    print(d)