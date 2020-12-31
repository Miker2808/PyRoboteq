from PyRoboteq import RoboteqHandler
from PyRoboteq import roboteq_commands as cmds
import keyboard # to run this library you need to be on root (run this python script as sudo)

controller = RoboteqHandler(debug_mode=True, exit_on_interrupt=False) 
connected = controller.connect("COM9") # Insert your COM port (for windows) or /dev/tty{your_port} (Commonly /dev/ttyACM0) for linux.

if __name__ == "__main__":
    while connected:
        
        if keyboard.is_pressed('s'):
            print("S pressed")
            drive_speed_motor_one = 200
            drive_speed_motor_two = 200
            
        else if keyboard.is_pressed('d'):
            print("D pressed")
            drive_speed_motor_one = 200
            drive_speed_motor_two = 200

        else if keyboard.is_pressed('x'):
            print("X is pressed")
            drive_speed_motor_one = -200
            drive_speed_motor_two = 200

        else if keyboard.is_pressed('c'):
            print("C is pressed")
            drive_speed_motor_one = 200
            drive_speed_motor_two = -200

        # Motor will automatically stop if no command is sent.
        else:
            drive_speed_motor_one = 0
            drive_speed_motor_two = 0

        controller.send_command(cmds.DUAL_DRIVE, drive_speed_motor_one, drive_speed_motor_two)
        
            
            

        
        

