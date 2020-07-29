# This file contains the full list of the commands used by the SDC21** motor driver series
# Each constant will be used as a message receiver or sender parameter (Send speed, read speed, etc..)
# Please refer to the roboteq official manual for more information: https://www.roboteq.com/docman-list/motor-controllers-documents-and-files/documentation/user-manual/272-roboteq-controllers-user-manual-v17/file
# IMPORTANT: These constants are for serial use

SET_ACCEL = "!AC" # Set Acceleration
NXT_ACCEL = "!AX" # Next Acceleration
SET_BOOL = "!B" # Bool Varialbe (Not in use)
SPEC_BIND = "!BIND"  # Spectrum Bind
SET_ENC_COUNTER = "!C" # Set encoder counter
SET_BL_COUNTER = "!CB" # Set brushless counter
SET_CANGO = "!CG" # Set motor command via CAN
CAN_SEND = "!CS" # Can send
CSS = "!CSS" # Set SSI Sensor Counter
DRES = "!D0" # reset individual digital outbits
DSET = "!D1" # Set individual digital outbits
DOUT = "!DS" # Set all digital outbits
NXT_DECEL = "!DX" # Next deceleration
EE_SAVE = "!EES" # Save configuration in EEPROM (Saves configuration in motor driver memory)
EM_STOP = "EX" # Initiate emergency stop
GO = "!G" # Got to speed or relative position
GO_TORQUE = "!GIQ" # Go to torque AMPs
GO_TORQUE_2 = "!QID" # Got to torque amps (It is recommended to use the manual before using these commands)
HOME_COUNTER = "!H" # Load home counter
REL_EM_STOP = "!MG" # Release emergency stop
STOP_ALL = "!MS" # Stop in all modes (will stop for channel)
MOT_POS = "!P" # Go to motor absolute desired position
MPOS_REL = "!PR" # Go to relative desired position
NXT_POSR = "!PRX" # NEXT go to relative desired position
NXT_POS = "PX" # NEXT go to absolute desired position
MICRORUN_BASIC = "!R" # MicroRun Basic (View manual for more info)
RC_OUT = "!RC" # Set Puls out
SET_SPEED = "!S" # Set motor speed
STO_SELF_TEST = "!SST" # STO self test
NXT_VELO = "!SX" # Set next velocity
VAR = "!VAR" # set user variable (View manual for more info)
DUAL_DRIVE = "!M" #Send Dual Drive command, one parameter for left and one for right side