from robotonomy import setup
from robotonomy import RoboPiLib as RPL

motorL = 0
motorR = 1

motorR_forward = 2000
motorR_backward = 1000
motorL_forward = 1000
motorL_backward = 2000

def forward():
  RPL.servoWrite(motorL,motorL_forward)
  RPL.servoWrite(motorR,motorR_forward)

def stop():
  RPL.servoWrite(motorL, 0)
  RPL.servoWrite(motorR, 0)

counter = 0
#Use time.time
while counter == 0