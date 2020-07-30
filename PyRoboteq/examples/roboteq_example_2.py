from PyRoboteq import RoboteqHandler
import time

controller = RoboteqHandler()
connected = controller.connect("COM9")

if __name__ == "__main__":
    while connected:
        controller.dual_motor_control(200, 200)
        

        
        

