from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import time
import keyboard

controller = RoboteqHandler()
connected = controller.connect("COM9") # Insert your COM port (for windows)

if __name__ == "__main__":
    drive_speed = 200

    while connected:
        #time.sleep(0.1)
        
        if keyboard.is_pressed('s'):
            print("S pressed")
            drive_speed = 200
            
        if keyboard.is_pressed('d'):
            print("D pressed")
            drive_speed = 200

        
        controller.send_raw_command(cmds.DUAL_DRIVE, drive_speed, drive_speed)
        
            
            

        
        

