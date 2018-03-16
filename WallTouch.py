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

def stop():
  RPL.servoWrite(motorL, 0)
  RPL.servoWrite(motorR, 0)

while counter == 0:

    RPL.analogRead(0)
    RPL.digitalRead(23)
    Analog = RPL.analogRead(0)
    digital = RPL.digitalRead(23)


    if digital == 1:

        forward()

    if digital == 0 and Analog > 450:
        RPL.servoWrite(motorL,1440)
        RPL.servoWrite(motorR,1560)

    if digital == 0 and Analog < 450 and Analog > 190:
        RPL.servoWrite(motorL,1470)
        RPL.servoWrite(motorR,1530)

    if digital == 0 and Analog < 191 and Analog > 4:
        RPL.servoWrite(motorL,1490)
        RPL.servoWrite(motorR,1510)

    if digital == 0 and Analog == 4:
        stop()
        counter = counter + 1
