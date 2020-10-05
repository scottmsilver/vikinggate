# hug.py

"""Basic API for managing the relays"""
import hug
import cmg
import logging

logging.basicConfig()

# To run:
#
#  hug -f api.py
#
# To test locally (enable and disable these relays)
#
#  curl -X PUT "http://localhost:8000/relay/2"
#  curl -X DELETE "http://localhost:8000/relay/2"

@hug.put('/relay/{number}')
def enableRelay(number: hug.types.number):
    """Enable a relay"""
    controller = cmg.GateController()
    controller.setRelay(number, True)
    return "Enabled Relay {0}".format(number)

@hug.delete('/relay/{number}')
def disableRelay(number: hug.types.number):
    """Disable a relay"""
    controller = cmg.GateController()
    controller.setRelay(number, False)
    return "Diabled Relay {0}".format(number)

