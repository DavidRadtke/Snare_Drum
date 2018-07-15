import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  #GPIO Nummern = Pin Nummer
GPIO.setwarnings(False)   #GPIO Fehler deaktivieren
                          #Pin 15 überwacht fallende Flanke
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                          #Pin steuert Relais zm an/abkoppeln des Motortreibers
GPIO.setup(40,GPIO.OUT)

                          #FUNKTION die aus den Programm "springt":
def tasterueberwachung(callback):
   GPIO.output(40,False)  #Relais abschalten
   print "callback"
   sys.exit(0)

                          #Falls event "FALLING" erkannt wird-> spingt in Funktion "tasterueberwachung"
GPIO.add_event_detect(15, GPIO.FALLING, callback=tasterueberwachung)
while 1:
                          #LED GELD leuchet:
   GPIO.setup(38,GPIO.OUT)
   GPIO.output(38,True)
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
                          #Relais/Motortreiber anschalten
   GPIO.output(40,True)
                          #Warten bis Relais geschaltet
   time.sleep(0.02)
                          #Motor läuft
   for i in range(99):
                for step in range(4):
                                time.sleep(0.0016)
                                GPIO.output(29, seq[step][0])
                                GPIO.output(31, seq[step][1])
                                GPIO.output(33, seq[step][2])
                                GPIO.output(35, seq[step][3])
                                print i
                          #GPIO's Reset
GPIO.cleanup()


