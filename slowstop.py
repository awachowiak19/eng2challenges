import setup
import RoboPiLib as RPL
import time

motorL = 0
motorR = 1

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

    RPL.digitalRead(17)

    obstacle = RPL.digitalRead(17)

    if obstacle == 1:

        forward()

    if obstacle == 0:
        time1 = time.time()
        RPL.servoWrite(motorL,1420)
        RPL.servoWrite(motorR,1580)

        if round(time.time(),0) - time1 == 1:
            time2 = time.time()
            RPL.servoWrite(motorL,1470)
            RPL.servoWrite(motorR,1530)

            if round(time.time() - time2,0) == 1:
                time3 = time.time()
                RPL.servoWrite(motorL,1490)
                RPL.servoWrite(motorR,1510)

                if round(time.time() - time3,0) == 1:
                    stop()



        counter = counter + 1
