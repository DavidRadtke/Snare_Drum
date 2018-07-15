import RPi.GPIO as GPIO
import time
import sys


GPIO.setwarnings(False)    #GPIO Warnungen deaktivieren
GPIO.setmode(GPIO.BOARD)   #GPIO Belegung entspricht Pin Belegung
                           #Motorsteuerungspins auf '0' setzen-> Motortreiberproblem umgehen
GPIO.setup(29,GPIO.OUT)
GPIO.output(29,False)
GPIO.setup(31,GPIO.OUT)
GPIO.output(31,False)
GPIO.setup(33,GPIO.OUT)
GPIO.output(33,False)
GPIO.setup(35,GPIO.OUT)
GPIO.output(35,False)
                           #LED GELB anschalten
GPIO.setup(38,GPIO.OUT)
GPIO.output(38,True)

while 1:
    c = sys.stdin.read(1)

    if c == '\n':

       GPIO.setmode(GPIO.BOARD)
                          # Grüne LED anschalten     
       GPIO.setup(22,GPIO.OUT)
       GPIO.output(22,True)
                          # Rote LED abschalten     
       GPIO.setup(11,GPIO.OUT)
       GPIO.output(11,True)
                          #Gelbe LED abschalten     
       GPIO.output(38,False)
                          # Relais auf '0' -> Motortreiber abkoppeln
       GPIO.setup(40,GPIO.OUT)
       GPIO.output(40,False)
      
                          #Pins für Motorsteuerung       
       ControlPin = [29,31,33,35]

       for pin in ControlPin:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,0)

                          #Sequenz für Schrittmotor
       seq =  [  [0,0,1,1],
                 [1,0,0,1],
                 [1,1,0,0],
                 [0,1,1,0] ]
                         #Motortreiber ankoppeln
       GPIO.output(40,True)
       time.sleep(0.02)
                         #Etwas mehr als eine Umdrehung fahren-> Stick schlagen und stoppen
       for i in range(57):
                   for step in range(4):
                                time.sleep(0.0016)
                                GPIO.output(29, seq[step][0])
                                GPIO.output(31, seq[step][1])
                                GPIO.output(33, seq[step][2])
                                GPIO.output(35, seq[step][3])
                                print(i)

                         #Nocke verharrt unten um Nachschwingen zu vermeiden
       time.sleep(0.2)
                         #Nocke fährt zurrück auf Grundposition       
       for i in range(8):
                     for step in range(4):
                                time.sleep(0.0016)
                                GPIO.output(29, seq[step][3])
                                GPIO.output(31, seq[step][2])
                                GPIO.output(33, seq[step][1])
                                GPIO.output(35, seq[step][0])
                                print(i)
       
                         #Relais öffnen / Motortreiber abkoppeln
       GPIO.output(40,False)
                         #Motorsteuerungspins auf '0' setzen       
       GPIO.output(29,False)
       GPIO.output(31,False)
       GPIO.output(33,False)
       GPIO.output(35,False)







