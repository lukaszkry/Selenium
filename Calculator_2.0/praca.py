# wmic bios get serialnumber#Windows
# hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid#Linux
# ioreg -l | grep IOPlatformSerialNumber#Mac OS X
import os
import sys
import subprocess

def create_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
    print("Created Directory : ", dir)
  else:
    print("Directory already existed : ", dir)
  return dir


def create_txt(path):
    os.chdir(path)
    with open('monitors.txt', 'w') as fp:
        pass

def run_ps1():
    p = subprocess.Popen(["powershell.exe",
                          "C:\\Users\\theri\PycharmProjects\\Selenium\\Calculator_2.0\\test.ps1"],
                         stdout=sys.stdout)
    p.communicate()

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

# output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX
create_dir('C:\\test')
create_txt('C:\\test')
run_ps1()
print(getMachine_addr())
print(user_name())
print(ram_clock())
