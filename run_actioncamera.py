import RPi.GPIO as GPIO
import time

buttonPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
  
  # variable 'count' use to know how long we press the button
  count=0

  # We use 'not' because the pull-up circuit
  # While the button is pressed, we increment the value
  while not (GPIO.input(buttonPin)): 
    sleep(50)
    count+=1 
  
  # if we press the button less than 250ms, so take a picture, otherwise take a video
  if (count<5 and count > 0): 
    print("Take a Picture")
  elif (count>5):
    print("Take a Video")

def sleep (x):
  time.sleep(x/1000)