from roboteq import RoboteqDevice
from roboteq.roboteq_constants import _MMOD, _G, _MXMD, _MXRPM, _RWD
import time
device = RoboteqDevice()
device.connect("COM9")

while True:
    device.command_motor(_G, 1, 1000)
    