""" ---- robo_controls.py ----  

This module handles all the automation controls 
for the delta robot. Each location for pickup,
sorting and image capture were presteremined.
Each function in this module represents one
movement the delta needs to make.

This module opens 2 COM ports, one that is used
for moving the end effector and another that is
used for controling the lighting rig and vacuum
pump.  The end effector locations are sent in 
(x, y, z) form to the main PCB where they are
translated into delta coordinates and sent to
stepper drivers. The lighting rig and vacuum pump
are handled by sending special characters to main
PCB.

These functions are designed to be called from
the GUI module.
-------------------------------"""
import grblProofOfConcept
import time

COM_0 = "COM3"  #variable holds name of COM Port used for sending (x, y, z) coordinates.
COM_1 = "COM2"  #variable holds name of COM Port used for sending special characters for vacuum pump and lighting rig.

#Open COM Ports
grblCOM = grblProofOfConcept.ArduinoSerialObj(COM_0)
light_pump_COM = grblProofOfConcept.ArduinoSerialObj(COM_1)

#Special characters for pump and lighting
pump_char = '^'
led_char =  '*'

#TODO add coordinates
#End effector coordinates
start_loc = "x0y0z0"
pass_loc = "x0y0z0"
fail_loc = "x0y0z0"
camera_loc = "x0y0z0"

delay_time = 0.5

def turn_on_vacuum():
    light_pump_COM.write(pump_char)
    print("Turning on vacuum pump")
    time.sleep(delay_time)    

def pickup():
    print("Picking up sample...")
    time.sleep(delay_time)
            
def drop():
    light_pump_COM.write(pump_char)
    print("Dropping sample...")
    time.sleep(delay_time)
            
def move_to_start():
    grblCOM.write(start_loc)
    print("Moving to Start...")
    time.sleep(delay_time)

def move_to_camera():
    grblCOM.write(camera_loc)
    print("Moving to Camera...")
    time.sleep(delay_time)

def move_to_pass():
    grblCOM.write(pass_loc)
    print("Moving to Pass Stack...")
    time.sleep(delay_time)
    
def move_to_fail():
    grblCOM.write(fail_loc)
    print("Moving to Fail Stack...")
    time.sleep(delay_time)
    
