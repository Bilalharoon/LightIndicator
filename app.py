from flask import Flask, render_template, request, redirect, url_for
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/led", methods=['POST'])
def led():  
    ledOn = request.form.get("led")
    print(ledOn)
    if ledOn == "on":
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)
    return redirect(url_for("index"))
    

if __name__ == "__main__":
    app.run(port=8000, debug=True, host="0.0.0.0")




