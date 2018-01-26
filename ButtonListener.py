import RPi.GPIO as GPIO
import time
import os
import FeederServo

#adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)

prev_input = 0 

    #this is the script that will be called (as root)

feeder=FeederServo

while True:
  #take a reading
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(buttonPin,GPIO.IN)
  binput = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and binput):
    print("Button pressed")
    feeder.feed()
#os.system("python /home/pi/feeder/CatFeeder-servo.py")
  #update previous input
  prev_input = binput
  #slight pause to debounce
  time.sleep(0.05)

