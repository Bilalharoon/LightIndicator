from flask import Flask, render_template, request, redirect, url_for
import RPi.GPIO as GPIO
import math
# pins: 18, 17, 4 BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/led", methods=['POST'])
def led():  
    light_selector = request.form["light-selector"]
    switch_light(light_selector)
    return redirect(url_for("index"))
    



def switch_light(color):
    light_dict = {
                "green":[18, False],
                "red":[17, False],
                "yellow":[4, False]
            }
    for led_color in light_dict:
        if led_color == color:
            GPIO.output(light_dict[led_color][0], GPIO.HIGH)
            light_dict[led_color][1] = True
        else:
            GPIO.output(light_dict[led_color][0], GPIO.LOW)
            light_dict[led_color][1] = False

if __name__ == "__main__":
    app.run(port=8000, debug=True, host="0.0.0.0")




