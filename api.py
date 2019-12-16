# hug.py

"""Basic API for managing the relays"""
import hug
import cmg
import logging

logging.basicConfig()

# To run:
#
#  hug -f hug.py
#
# To test locally (enable and disable these relays)
#
#  curl -X PUT "http://localhost:8000/relay/2"
#  curl -X DELETE "http://localhost:8000/relay/2"

@hug.put('/relay/{number}')
def enableRelay(number: hug.types.number):
    """Enable a relay"""
    relay = cmg.GateController.Relay(number)
    controller = cmg.GateController()
    controller.setRelay(relay, True)

@hug.delete('/relay/{number}')
def disableRelay(number: hug.types.number):
    """Disable a relay"""
    relay = cmg.GateController.Relay(number)
    controller = cmg.GateController()
    controller.setRelay(relay, False)


