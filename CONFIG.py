machine = 'merlin'
# machine = 'batterylab'
local = True


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
    server = "JOHNLAPTOP\SQLEXPRESS"
    # server = "dt-sql03"
    db = "batterylab_finaltest"        
    report_folder_roots = []