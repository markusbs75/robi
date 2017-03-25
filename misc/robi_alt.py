#!/usr/bin/python3
from time import sleep
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# Funktion, um alle genutzten Pins auf Low zu schalten
def all_off():                                                                  
    GPIO.output(EnableA, False)
    GPIO.output(EnableB,False)
    GPIO.output(Input1,False)
    GPIO.output(Input2,False)
    GPIO.output(Input3,False)
    GPIO.output(Input4,False)
    return

def vor():
    GPIO.output(EnableA,True)
    GPIO.output(EnableB,True)
    GPIO.output(Input1,True)
    GPIO.output(Input2,False)
    GPIO.output(Input3,True)
    GPIO.output(Input4,False)

def zurueck():
    GPIO.output(EnableA,True)
    GPIO.output(EnableB,True)
    GPIO.output(Input1,False)
    GPIO.output(Input2,True)
    GPIO.output(Input3,False)
    GPIO.output(Input4,True)

def rechts():
    GPIO.output(EnableA,True)
    GPIO.output(EnableB,True)
    GPIO.output(Input1,True)
    GPIO.output(Input2,False)
    GPIO.output(Input3,False)
    GPIO.output(Input4,True)


def links():
    GPIO.output(EnableA,True)
    GPIO.output(EnableB,True)
    GPIO.output(Input1,False)
    GPIO.output(Input2,True)
    GPIO.output(Input3,True)
    GPIO.output(Input4,False)


# Den GPIO-Pins werden die Namen der L298-Eingänge zugewiesen.
EnableA = 13                                                                    
EnableB = 15
Input1  = 3
Input2  = 5
Input3  = 7
Input4  = 11


# Alle genutzten GPIO-Pins als Ausgang deklarieren.
GPIO.setup(EnableA,GPIO.OUT)                                                    
GPIO.setup(EnableB,GPIO.OUT)
GPIO.setup(Input1,GPIO.OUT)
GPIO.setup(Input2,GPIO.OUT)
GPIO.setup(Input3,GPIO.OUT)
GPIO.setup(Input4,GPIO.OUT)


# Funktion "all_off" aufrufen
all_off()                                                                       


try:

	while True:
		# Eingabefeld zur Motorauswahl.
		# Groß-/Kleinschreibung beachten.
		motor = input("Geben Sie die Richtung ein ein: 'a(links)', 's(rechts)','w (vor)' oder 'y (zurück)': ")

		# if-Schleifen zur Abfrage der vorherigen Eingabe
		if motor == "w":
			vor()                                    
			sleep (1)           # Motor dreht jeweils 5 Sekunden.
			all_off() 
		if motor == "y":
			zurueck()                                    
			sleep (1)           # Motor dreht jeweils 5 Sekunden.
			all_off()
		if motor == "a":
			links()                                    
			sleep (0.1)           # Motor dreht jeweils 5 Sekunden.
			all_off()
		if motor == "s":
			rechts()                                    
			sleep (0.1)           # Motor dreht jeweils 5 Sekunden.
			all_off() 
	
			
# beim Programmende durch Strg+C wird "all_off" ausgeführt
except KeyboardInterrupt:                                                       
    all_off()
