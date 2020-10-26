# PyRoboteq

Python library to ease with roboteq motor driver programming


## Installation

PyRoboteq is currently still in development and is not yet available in PyPi (similar libraries are available).
To install the library you'll have to simply download the files and import them from their path


## Requirements 

**Important:** this library was tested currently only on SDC2130 motor controller, and will probably support only the SDC21** series
To make sure your motor controller will work, you'll need the following:
installed PySerial module (imported as 'serial')
connection to the motor controller via serial communication (a usb)


## Usage

Import the PyRoboteq package
```python
from roboteq_handler import RoboteqHandler
```
If you want to use additional commands instead of writing them manually, you will have to additionaly import the roboteq connections file
```python
import roboteq_commands
```
To connect to the controller you'll have to make a controller object, and additionally connect to it.
```python
controller = RoboteqHandler()  # Create controller object
controller.connect("COM9") # connect to the controller (COM9 is an example for windows)
```
Then what you will have to do is to simply write a command to the motors, if you have the SDC2130 dual series, you'll be able to communication with 2 motors
```python
if __name__ == "__main__":
    while True:
        controller.dual_motor_control(100, 100) # Send command to the controller
```

If you want to send a raw message to the controller you can use the send_raw_command
```python
controller.send_raw_command(EM_STOP) # this will send 0 argument command for emergency stop
controller.send_raw_command(REL_EM_STOP) # send this command to release it
controller.send_raw_command(SET_SPEED, 1, 1000) # send set speed command to channel 1 (first argument) with the value of up to 1000 RPM (second argument)
```
As you can notice, you do not have to use all the arguments, check the manual to see how many arguments you need to use in the manual.

## More information
For more information please refer to the manual listed [here](https://www.roboteq.com/docman-list/motor-controllers-documents-and-files/documentation/user-manual/272-roboteq-controllers-user-manual-v17/file)

## License
[MIT License](https://choosealicense.com/licenses/mit/)

