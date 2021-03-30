#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import time
import threading
import os

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(12,GPIO.OUT)
p = GPIO.PWM(12,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
 

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/open")
def open():
    p.start(0)
    duty = 90 / 18 + 2
    p.ChangeDutyCycle(7)
    time.sleep(1)
    p.ChangeDutyCycle(0)
    return Response({"wat":"wat"})

@app.route("/close")
def close():
    p.start(7)
    print("hit")
    p.ChangeDutyCycle(0)
    time.sleep(0.5)
    p.stop()
    return Response({"wat":"wat"})

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(12, True)
	p.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(12, False)
	p.ChangeDutyCycle(0)

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
    


