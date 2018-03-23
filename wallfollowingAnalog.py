import setup
import RoboPiLib as RPL

motorL = 1
motorR = 2

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

counter = 0

def forward():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,motorR_forward)

def reverse():
    RPL.servoWrite(motorL,motorL_backward)
    RPL.servoWrite(motorR,motorR_backward)

def stop():
  RPL.servoWrite(motorL, 0)
  RPL.servoWrite(motorR, 0)

while counter == 0:
    RPL.analogRead(0)
    RPL.analogRead(3)
    Fanalog = RPL.analogRead(0)
    Banalog = RPL.analogRead(3)

    straight = Fanalog - Banalog

    if straight > -2 and straight < 8:
        reverse()
#if the robot is angled away the wall- turn tiwards
    if straight < -2:
        RPL.servoWrite(motorL,1550)
        RPL.servoWrite(motorR,motorR_backward)
#if the robot is towards  the wall
    if straight > 8:
        RPL.servoWrite(motorL,motorL_backward)
        RPL.servoWrite(motorR,1450)
