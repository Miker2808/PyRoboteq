from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
import keyboard # to run this library you need to be on root (run this python script as sudo)

controller = RoboteqHandler()
connected = controller.connect("/dev/ttyACM0") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

if __name__ == "__main__":
    drive_speed = 0
    print("Press S to stop")
    print("Press D to drive")
    while connected:
        
        if keyboard.is_pressed('s'):
            #print("S pressed")
            drive_speed = 0
            
        if keyboard.is_pressed('d'):
            #print("D pressed")
            drive_speed = 250

        
        controller.send_command(cmds.DUAL_DRIVE, drive_speed, drive_speed)
        battery_amps = controller.read_value(cmds.READ_BATTERY_AMPS, 1) # Read value 1 of battery amps
        print(battery_amps)
            
            

        
        

