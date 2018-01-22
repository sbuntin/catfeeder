import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

prev_input = 0 

    #this is the script that will be called (as root)

while True:
  #take a reading
  input = GPIO.input(buttonPin)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
    os.system("python /home/pi/feeder/CatFeeder-servo.py")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)
