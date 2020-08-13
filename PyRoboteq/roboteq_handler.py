import serial
import time
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
            print("ERROR: Failed to connect to the roboteq device, read the exception error below:")
            print(e)
            print("\n\n")
            self.is_alive = False
        
        return self.is_alive

    def send_raw_command(self, str_command: str = "") -> None:
        """
        Send a raw string command, the library will handle sending the command, but how you write it
        is up to you.
        """
        raw_command = f"{str_command}+\r"
        try:
            self.ser.write(raw_command.encode())

        except Exception as e:
            print("Failed to send command to the controller, read the exception error below:")
            print(e)
            print("\n\n")
        
    def request_handler(self, request: str = "") -> str:
        """
        Sends a command and a parameter, 
        """
        def get_data(serial):
            raw_data = b''
            while raw_data == b'':
                try:
                    raw_data = serial.read_all()
                except Exception as e:
                    print("Failed to read from the controller, read the exception error below:")
                    print(e)
                    print("\n")
                    raw_data = b' '
            return raw_data

        self.send_raw_command(request)
        result = get_data(self.ser)
        result = result.decode()
        result = result.split("\r")

        return result[1]

    def dual_motor_control(self, left_motor: int = 0, right_motor: int = 0) -> None:
        """
        Controlling the motor using a Dual Drive mode
        Send speed for the left, and right side of the robot/vehicle seperately 
        Effective for doing Pivot drive and running track based robots
        left_motor: integer from -1000 to 1000
        right_motor: integer from -1000 to 1000
        """
        #raw_command = "!M " + str(left_motor) + " " + str(right_motor) + "\r"
        raw_command = f"!M {left_motor} {right_motor} "
        self.request_handler(raw_command)
    
    def read_value(self, command: str = "", parameter = "") -> str:
        request = f"{command} [{parameter}]"
        response = self.request_handler(request)
        return response