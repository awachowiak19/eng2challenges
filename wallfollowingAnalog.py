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

def turnL():
      RPL.servoWrite(motorL,1460)
      RPL.servoWrite(motorR,motorR_forward)

def turnR():
      RPL.servoWrite(motorL,motorL_forward)
      RPL.servoWrite(motorR, 1540)

while counter == 0:
    distance = RPL.analogRead(0)

    if distance > 254 and distance < 284:
        reverse()

    if distance < 285:
        RPL.servoWrite(motorL,1530)
        RPL.servoWrite(motorR,motorR_backward)

    if distance > 250:
        RPL.servoWrite(motorL,motorL_backward)
        RPL.servoWrite(motorR,1470)
