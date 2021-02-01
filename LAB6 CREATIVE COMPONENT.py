from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
import time
from time import sleep

camera = PiCamera()

password=1234

userpw=input('please punch in a 4 digits code and press enter')
entry=int(userpw)
    
if entry==password:
    print('Success')
else:
    print('Failure')
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % timestamp)
    pause()
        







