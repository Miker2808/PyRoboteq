# PyRoboteq [![Downloads](https://static.pepy.tech/badge/PyRoboteq)](https://pepy.tech/project/PyRoboteq)

Python library to ease with roboteq motor controllers programming


## Installation

Install the python package using: ```pip install PyRoboteq``` 

Alternatively, you can clone this repository and import from the "PyRoboteq" directory.

## Requirements 

**Tested Controllers**: SDC2130, SBL2360T

The library *may* work with additional roboteq controllers.

In order to work with your motor controller, you'll need the following:

* Installed PySerial module (imported as 'serial')
* Connection to the motor controller via serial communication (USB)
* Python 3.6 and above is recommended.

## Usage
### Setup
Import the PyRoboteq package
```python
from PyRoboteq import RoboteqHandler
```
The PyRoboteq library includes a set of commands which you can use, including a comment describing the use of the command.
To use the commands add the following line:
```python
from PyRoboteq import roboteq_commands as cmds
```

### Connection

In order to communicate with the controller, you will need to create a RoboteqHandler object, and then establish a connection with it.
The ```RoboteqHandler()``` class additionally supports two parameters which can ease with the development.
* The debug_mode parameter, which prints out any information sent or received to and from the controller, including any exceptions received.
* The ```exit_on_interrupt```. By default, the pyroboteq will ignore any exceptions to make sure minor interruptions wont crash your robot.
this can be averted by adding the ```exit_on_interrupt``` parameter to exit when any interruption is received.

```python
controller = RoboteqHandler(debug_mode = True, exit_on_interrupt = False)  # Create the controller object
```

The ```connect()``` method allows the library to connect to the controller, you must specifiy the port. The library
works both on linux and windows.

```python
is_connected = controller.connect("COM9") # connect to the controller (COM9 is an example for windows)
```

### Sending Commands

Afterwards, what you will have to do is to simply write a command to the motors, if you have the SDC2130 dual series, you'll be able to communicate with 2 motors 
```python
if __name__ == "__main__":
    while True:
        controller.dual_motor_control(100, 100) # Send command to the controller
```

To send a message to the controller, use the ```send_command()```
```python
controller.send_command(EM_STOP) # this will send 0 argument command for emergency stop
controller.send_command(REL_EM_STOP) # send this command to release it
controller.send_command(SET_SPEED, 1, 1000) # send 'set speed' command to channel 1 (first argument) with the value of up to 1000 RPM (second argument)
```
As you can notice, you do not have to use all the arguments, check the manual to see how many arguments you need to use.
The library will construct a command depending on how many arguments you give.

Even though ```send_command``` supports using raw strings, you can more preferablly send a raw string to the controller using the ```send_raw_command()``` method.
```python
controller.send_raw_command("!M 200 200") # send a raw string.
```

### Reading Commands

Sending commands to the controller is cool, but it would be much cooler, if the controller could also return you its very beneficial data.
For this, you can use the ```read_value()``` method. The method has 2 parameters, the read command, and optionally a parameter.
some commands will give you multiple data, like controller voltage, which will give you voltage from 3 different points of the controller.
It is recommended that you read the manual to see what each value means.
```python
controller_volts = controller.read_value(cmds.READ_VOLTS) # receive voltages from the controller
>>> "V= 12:16:5" # Without a parameter, the controller returns 3 channels, (internal, battery, 5v output) respectively
controller_volts = controller.read_value(cmds.READ_VOLTS, 2)
>>> "V= 16" # This way, the controller will return only the value of channel 2 (battery voltage)
```
Same command can be sent using a raw string:
```python
controller_volts = controller.read_value("?V", 2)
>>> "V=16"
```

## Examples
The PyRoboteq library comes with little examples which you can run right away.

To access the examples head to the "examples" directory inside the "PyRoboteq" directory.

## More information
For more information and manuals, please refer to the official Roboteq website.

## License
[MIT License](https://choosealicense.com/licenses/mit/)


Special thanks to everyone who contributed to this little project