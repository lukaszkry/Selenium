# wmic bios get serialnumber#Windows
# hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid#Linux
# ioreg -l | grep IOPlatformSerialNumber#Mac OS X
import os
import sys


def getMachine_addr():
    os_type = sys.platform.lower()
    if "win" in os_type:
        command = "wmic baseboard get serialnumber"
    elif "linux" in os_type:
        command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
    elif "darwin" in os_type:
        command = "ioreg -l | grep IOPlatformSerialNumber"
    return os.popen(command).read().replace("\n", "")


# output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX
print(getMachine_addr())

