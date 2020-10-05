import RPi.GPIO as GPIO
import time
from enum import Enum

class RelayBank:
    def __init__(self, relayPinList):
        self.relayPinList = relayPinList
        
        GPIO.setmode(GPIO.BOARD)
        for relayPin in self.relayPinList:
            GPIO.setup(relayPin, GPIO.OUT)

    def setRelay(self, relay, enabled):
        GPIO.output(self.relayPinList[relay], GPIO.LOW if enabled else GPIO.HIGH)
    
RELAY_PIN_LIST = [24, 21, 19, 23]    

class GateController:
    def setRelay(self, relayNumber, state):
        print("R(%d): %d" % (relayNumber, state))
        self.relayBank.setRelay(relayNumber, state)
        
    def __init__(self):
        # These are the pins on the RPI for the relays
        self.relayBank = RelayBank(RELAY_PIN_LIST)

def test():     
    controller = GateController()

    state = True
    while True:
        time.sleep(1)
        controller.setRelay(0, state)
        time.sleep(1)
        controller.setRelay(1, state)
        time.sleep(1)
        controller.setRelay(2, state)    
        state = not state


#test()
