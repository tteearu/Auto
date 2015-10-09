
# encoding: utf-8 
BODY = '''
<html>
    <head>
        <meta charset="UTF-8">
        <script type="text/javascript">
            function slide(duty_cycle) {
                window.location = "/" + duty_cycle;
            }
        </script>
    </head>
    <body> Thunderstruck!! <br>  
        <input type="range" min="0" max="100" value="%(duty_cycle)s" onChange="slide(this.value);"/>        
        <a href="/on">Mootor tööle</a><br>
        <a href="/off">Mootor seis</a><br>
    </body>
</html>
'''
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

r = GPIO.PWM(10, 500)  # RED   channel=10 frequency=500Hz
g = GPIO.PWM(22, 500)  # GREEN channel=22 frequency=500Hz
b = GPIO.PWM(27, 500)  # BLUE  channel=27 frequency=500Hz
r.start(100)
g.start(100)
b.start(100)


# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server

# Function that is ran when a http request comes in
def simple_app(env, start_response):
    
    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')] 
    start_response(status, headers)

    duty_cycle = 0

    # What did the user ask for?
    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        r.ChangeDutyCycle(0)


    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")  
        r.ChangeDutyCycle(100)

    else:
        duty_cycle = int(env["PATH_INFO"][1:])
        r.ChangeDutyCycle(100-duty_cycle)
        print("user asked for something else")
    return BODY % locals()



# Create a small python server
httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8000" 
httpd.serve_forever()
r.stop()
g.stop()
b.stop()
