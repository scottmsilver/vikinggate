import RPi.GPIO as GPIO
import time

# A bank of relays numbered from zero to len(relayPinList)
class RelayBank:
    # relayPinList is an array of pins (not GPIO numbers) to turn on.
    # Relay 0 is relayPinList[0], etc.
    def __init__(self, relayPinList):
        self.relayPinList = relayPinList
        
        GPIO.setmode(GPIO.BOARD)
        for relayPin in self.relayPinList:
            GPIO.setup(relayPin, GPIO.OUT)

    # Set the state of relayNumber to enabled.
    def setRelay(self, relayNumber, enabled):
        # The sense of enabled/disabled is opposite for these relays, which is
        # is why wwe invert enabled (as in GPIP.LOW if enabled)
        GPIO.output(self.relayPinList[relayNumber], GPIO.LOW if enabled else GPIO.HIGH)

# This is the ordered list of relays to pins (not GPIO numbers)
# Relay 0 is the first, etc.
RELAY_PIN_LIST = [24, 21, 19, 23]    

# Eventually this will have methods corresponding to functions o the gate.
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
        for x in range(len(RELAY_PIN_LIST)):
            time.sleep(1)
            controller.setRelay(x, state)
        state = not state            

test()
