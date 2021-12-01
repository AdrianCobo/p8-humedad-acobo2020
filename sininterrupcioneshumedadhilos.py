import RPi.GPIO as GPIO
import time
import threading
import signal
import sys

sensorHumedad = 16
ledVerde=20
ledRojo=21

def callbackSalir (senial, cuadro): # señal y estado cuando se produjo la interrup.
    pwm.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    GPIO.cleanup () # limpieza de los recursos GPIO antes de salir
    sys.exit(0)

def actuar_segun_Humedad ():

    flag1=False
    flag2=False

    while True:

        if not GPIO.input(sensorHumedad) and flag1 == False:
            print ("Ya tengo suficiente agua, gracias ;)")
            pwm2.ChangeDutyCycle(0)
            flag1=True
            flag2=False
        elif GPIO.input(sensorHumedad) and flag2 == False:
            print ("Necesito agua!!!!!!!")
            pwm2.ChangeDutyCycle(100)
            flag2=True
            flag1=False
        time.sleep(0.1)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(sensorHumedad, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #indicamos que el pin que vamos a usar para los leds , va a ser de salida
    GPIO.setup (ledVerde, GPIO.OUT)
    GPIO.setup (ledRojo, GPIO.OUT)
    #creamos un objeto PWM con los pines de los leds a usar y la frecuencia de trabajo como parametros:
    pwm = GPIO.PWM(ledVerde,100)
    pwm2 = GPIO.PWM(ledRojo,100)

    pwm.start (100)
    pwm2.start (0)

    hilo1 = threading.Thread(target=actuar_segun_Humedad)
    hilo1.start()

    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()