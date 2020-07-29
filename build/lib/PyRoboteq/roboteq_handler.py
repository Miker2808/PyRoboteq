import serial

class RoboteqHandler:
    """
    Create a roboteq device object for communication, read the README for more information
    """

    def __init__(self):
        self.is_alive = False
        self.port = ""
        self.baudrate = 115200
        self.ser = None
    
    def connect(self, port: str, baudrate: int = 115200) -> bool:
        """
        Attempt to establish connection with the controller
        """
        self.port = port
        self.baudrate = baudrate
        try:
            self.ser = serial.Serial(
                port = self.port,
                baudrate = self.baudrate,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE,
                bytesize= serial.EIGHTBITS
            )
            if self.ser.isOpen():
                self.ser.close()
            self.ser.open()
            self.is_alive = True

        except Exception as e:
            print("ERROR: Failed to connect to the roboteq device, read the exception error below..\n")
            print(e)
            print("\n\n")
            self.is_alive = False
        
        return self.is_alive

    def dual_motor_control(self, left_motor: int = 0, right_motor: int = 0) -> None:
        """
        Controlling the motor using a Dual Drive mode
        Send speed for the left, and right side of the robot/vehicle seperately 
        Effective for doing Pivot drive and running track based robots
        left_motor: integer from -1000 to 1000
        right_motor: integer from -1000 to 1000
        """
        raw_command = "!M " + str(left_motor) + " " + str(right_motor) + "\r"
        try:
            self.ser.write(raw_command.encode())
        except Exception as e:
            print("Failed to send command to the controller, read the exception error below..\n")
            print(e)
            print("\n\n")
    
    def send_raw_command(self, command: str = "", first_argument: str = "", second_argument: str = "") -> None:
        """
        Send raw commands, this is the default method, using the roboteq_commands list you can choose a command
        and write its arguments, at max there are just 2 arguments, using the manual, find out
        how many arguments you need to use, those you dont need, just leave blank
        """
        
        raw_command_0 = f"{command} {first_argument} {second_argument}\r"
        raw_command_1 = f"{command} {first_argument}\r"
        raw_command_2 = f"{command}\r"
        if first_argument == "" and second_argument == "":
            raw_command = raw_command_2
        elif first_argument is not "" and second_argument == "":
            raw_command = raw_command_1
        else:
            raw_command = raw_command_0

        try:
            self.ser.write(raw_command.encode())
        except Exception as e:
            print("Failed to send command to the controller, read the exception error below..\n")
            print(e)
            print("\n\n")
    