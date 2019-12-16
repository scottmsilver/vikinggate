import RPi.GPIO as GPIO
import time
from enum import Enum
    
class GateController:
    class Relay(Enum):
        ONE = 1, 37    # P25 = GPIO26, Pin 37
        TWO = 2, 38    # P28 = GPIO20, Pin 38
        THREE = 3, 40  # P29 = GPIO21, Pin 40

        def __new__(clazz, relay, pin):
            obj = object.__new__(clazz)
            obj._value_ = relay
            obj.pin = pin
            return obj
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for relay in GateController.Relay:
            GPIO.setup(relay.pin, GPIO.OUT)

    def setRelay(self, relay, high):
        GPIO.output(relay.pin, GPIO.HIGH if high else GPIO.LOW)

def test():     
    controller = GateController()

    state = True
    while True:
        time.sleep(1)
        controller.setRelay(GateController.Relay.ONE, state)
        time.sleep(1)
        controller.setRelay(GateController.Relay.TWO, state)
        time.sleep(1)
        controller.setRelay(GateController.Relay.THREE, state)    
        state = not state

test()
