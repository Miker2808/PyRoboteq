from roboteq_handler import RoboteqHandler
import time

controller = RoboteqHandler()
controller.connect("COM9")

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        controller.dual_motor_control(100, 100)

        
        

        