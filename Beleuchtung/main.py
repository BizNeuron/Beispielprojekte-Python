from machine import Pin
from time import sleep, sleep_ms
from random import randint
from keypad import KeyPad

led1_pin = 0  # Links vorne oben
led2_pin = 1  # Links vorne unten
led3_pin = 2  # Links hinten oben
led4_pin = 3  # Links hinten unten
led5_pin = 4  # Rechts vorne oben
led6_pin = 5  # Rechts vorne unten
led7_pin = 6  # Rechts hinten oben
led8_pin = 7  # Rechts hinten unten

led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)
led3 = Pin(led3_pin, Pin.OUT)
led4 = Pin(led4_pin, Pin.OUT)
led5 = Pin(led5_pin, Pin.OUT)
led6 = Pin(led6_pin, Pin.OUT)
led7 = Pin(led7_pin, Pin.OUT)
led8 = Pin(led8_pin, Pin.OUT)

leds = (led1, led2, led3, led4, led5, led6, led7, led8)

keyPad = KeyPad()

mode_id = -1 # -1 = no mode

def leds_on(delay=0):
    for i in range(0, 8):
        leds[i].on()
        sleep(delay)

def leds_off(delay=0):
    for i in range(0, 8):
        leds[i].off()
        sleep(delay)
        
def key():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print(keyvalue, end="\t")
        sleep_ms(300)
        return keyvalue
        
def mode_blink(delay=0.2):  # mode_id 0
    leds_on()
    sleep(delay)
    leds_off()
    sleep(delay)
    
def mode_random(delay=0.05):  # mode_id 1
    r_led1 = leds[randint(0,7)]
    r_led2 = leds[randint(0,7)]
    r_led3 = leds[randint(0,7)]
    r_led4 = leds[randint(0,7)]
    
    r_led1.on()
    r_led2.on()
    r_led3.on()
    r_led4.on()
    
    sleep(delay)
    
    r_led1.off()
    r_led2.off()
    r_led3.off()
    r_led4.off()
    
def mode_input(input_key=None): # mode_id 2
    if not input_key:
        input_key = key()
        
    led = -1
    
    if input_key == "1":
        led = 0
    elif input_key == "2":
        led = 1
    elif input_key == "3":
        led = 2
    elif input_key == "4":
        led = 3
    elif input_key == "5":
        led = 4
    elif input_key == "6":
        led = 5
    elif input_key == "7":
        led = 6
    elif input_key == "8":
        led = 7
    
    if led == -1:
        pass
    elif leds[led].value() == 0:
        leds[led].on()
    elif leds[led].value() == 1:
        leds[led].off()
        

while True:
    function_key = key()
    
    if function_key == "D":
        leds_off()
        mode_id = -1
    elif function_key == "A":
        mode_id = 0
    elif function_key == "B":
        mode_id = 1
    elif function_key == "C":
        mode_id = 2
        
    if mode_id == 0:
        mode_blink()
    elif mode_id == 1:
        mode_random()
    elif mode_id == 2:
        mode_input(function_key)
    