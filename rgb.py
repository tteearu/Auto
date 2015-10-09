import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

r = GPIO.PWM(10, 500)  # RED   channel=10 frequency=500Hz
g = GPIO.PWM(22, 500)  # GREEN channel=22 frequency=500Hz
b = GPIO.PWM(27, 500)  # BLUE  channel=27 frequency=500Hz
r.start(0)
g.start(0)
b.start(0)
try:
    while 1:       
	for dc in range(100, -1, -5):
            	r.ChangeDutyCycle(dc)
		time.sleep(0.1)
		print ("r.ChangeDutyCycle(", dc, ")")
	for dc in range(100, -1, -5):
		g.ChangeDutyCycle(dc)
		time.sleep(0.1)
		print ("g.ChangeDutyCycle(", dc, ")")
	for dc in range(100, -1, -5):
		b.ChangeDutyCycle(dc)
            	time.sleep(0.1)
		print ("b.ChangeDutyCycle(", dc, ")")   
	for dc in range(0, 101, 5):
            	r.ChangeDutyCycle(dc)		
		time.sleep(0.1)
		print ("r.ChangeDutyCycle(", dc, ")")
	for dc in range(0, 101, 5):
		g.ChangeDutyCycle(dc)
		time.sleep(0.1)
		print ("g.ChangeDutyCycle(", dc, ")")
	for dc in range(100, -1, -5):
            	r.ChangeDutyCycle(dc)
		time.sleep(0.1)
		print ("r.ChangeDutyCycle(", dc, ")")
	for dc in range(0, 101, 5):
		b.ChangeDutyCycle(dc)
            	time.sleep(0.1)
		print("b.ChangeDutyCycle(", dc, ")")
	for dc in range(50, 100, 5):
            	r.ChangeDutyCycle(dc)
		time.sleep(0.1)
		print("r.ChangeDutyCycle(", dc, ")")

except KeyboardInterrupt:
    pass
r.stop()
g.stop()
b.stop()
GPIO.cleanup()

