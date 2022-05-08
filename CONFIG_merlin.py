import logging
machine = 'merlin'
# machine = 'batterylab'
local = True

logging.basicConfig(filename='harvest.log',level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt="%m/%d/%Y %H:%M:%S")

if machine == 'merlin':
    server = "dt-sql03"
    db = "batterylab_finaltest"
    table = "MERLIN"
    report_folder_roots = ['C:\\PTM820eSystem\\Runtime\\Toyota Prius Battery_Gen2\\Test Sequence Logs\\',
              'C:\\PTM820eSystem\\Runtime\\Toyota Prius Battery_Gen3\\Test Sequence Logs\\']
    Trusted_ConnectionStr = ''
    if local:
        server = "JOHNLAPTOP\SQLEXPRESS"
        report_folder_roots = ['C:\\work\\pyHarvest\\reports\\']
        Trusted_ConnectionStr = 'Trusted_Connection=yes;'

else:
    # server = "JOHNLAPTOP\SQLEXPRESS"
    server = "dt-sql03"
    db = "batterylab_finaltest"  
    table = "BATTERYLAB"      
    Trusted_ConnectionStr = ''
    report_folder_roots = ['M:\\Battery Test System\\Reports']
    if local:
        server = "JOHNLAPTOP\SQLEXPRESS"
        report_folder_roots = ['C:\\work\\pyHarvest\\reports_batterylab']
        Trusted_ConnectionStr = 'Trusted_Connection=yes;'