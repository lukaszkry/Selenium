import os
import sys
import subprocess
import pandas as pd

global data
data = []

def main_dir():
    cwd = os.getcwd()
    return cwd

def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print("Created Directory : ", dir)
    else:
        print("Directory already existed : ", dir)
    return dir

def create_txt(path):
    os.chdir(path)
    with open('monitors.txt', 'w') as f:
        f.close()
        pass

def run_ps1(path):
    os.chdir(path)
    p = subprocess.Popen(["powershell.exe",
                          "C:\\Ewidencja\\test.ps1"],
                         stdout=sys.stdout)
    p.communicate()

def read_txt(path):
    os.chdir(path)
    read_file = pd.read_csv('monitors.txt', encoding='utf-16').replace(" ", "")
    read_file.to_csv('monitors.csv', index=None)

def getMachine_addr():
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic baseboard get serialnumber"
    elif "linux" in os_type:
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command).read().replace("\n", "")

def user_name():
    os_type = sys.platform.lower()
    return os.popen("whoami").read().replace("\n", "").replace("\\", "  ")

def ram_clock():
    os_type = sys.platform.lower()
    return os.popen("wmic memorychip get speed").read().replace("\n", "").replace("\\", "  ")


directory = main_dir()
create_dir('C:\\Ewidencja')
create_txt('C:\\Ewidencja')
run_ps1('C:\\Ewidencja')
read_txt('C:\\Ewidencja')
getMachine_addr()
user_name()
ram_clock()
