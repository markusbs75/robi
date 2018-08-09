#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Pin-Nummern verwenden (nicht GPIO-Nummern!)
GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)

# Pin 29 (= GPIO 21) zur Datenausgabe verwenden
GPIO.setup(29, GPIO.OUT)

while True:
	# Pin 29 einschalten
	GPIO.output(29, GPIO.HIGH)
	# Pin 29 nach fünf Sekunden wieder ausschalten
	time.sleep(1)
	GPIO.output(29, GPIO.LOW)
	time.sleep(1)

# alle vom Script benutzten GPIOs/Pins wieder freigeben
GPIO.cleanup()

