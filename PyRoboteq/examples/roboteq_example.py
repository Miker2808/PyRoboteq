from PyRoboteq import RoboteqHandler
import time

controller = RoboteqHandler()
connected = controller.connect("COM9") # Insert your COM port (for windows)

if __name__ == "__main__":
    while connected:
        time.sleep(0.1)
        controller.dual_motor_control(200, 200)
        

        
        

