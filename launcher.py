import os, psutil

def processRunning(processName):                                                                                                        #   determines wheather a process is running or not
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


forzaPath = "G:\XBOX_GAMES\Forza Horizon 5\Content\ForzaHorizon5.exe"                                                                   #   The path to your Forza executable(right click on the.exe and click copy as path)
os.system("""for /F "skip=3 tokens=3*" %G in ('netsh interface show interface') do (netsh interface set interface %H disable)""")       #   Disable all network adapters
os.system(""" "{}" """.format (forzaPath))                                                                                              #   Start Forza
while(not processRunning("forzahorizon5.exe")):                                                                                         #   Wait untill Forza starts
    pass
os.system("""for /F "skip=3 tokens=3*" %G in ('netsh interface show interface') do (netsh interface set interface %H enable)""")        #   Enable all network adapters