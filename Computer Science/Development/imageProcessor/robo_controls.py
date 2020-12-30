import time
import GRBL

start_crdnts_up = {} #start coordinates
start_crdnts_dn = {} #start coordinates

pass_crdnts_up = {} #test pass stack
pass_crdnts_dn = {} #test pass stack

fail_crdnts_up = {} #test fail stack
fail_crdnts_dn = {} #test fail stack

camera_cordnts_up = {} #camera locations
camera_cordnts_dn = {} #camera locations


#Controls functions for the delta
sleep_time = 0.5

def turn_on_vacuum():
    print("Turning on vacuum pump")  

def pickup():
    print("Picking up sample...")
    time.sleep(sleep_time)
            
def drop():
    #for x in range(0, SIZE, 1):
        #grblCom1.write(CONT_MAT1[x])
    print("Dropping sample...")
    time.sleep(sleep_time)
            
def move_to_start():
    print("Moving to Start...")
    time.sleep(sleep_time)

def move_to_camera():
    print("Moving to Camera...")
    time.sleep(sleep_time)

def move_to_passed():
    print("Moving to Pass Stack...")
    time.sleep(sleep_time)
    
def move_to_failed():
    print("Moving to Fail Stack...")
    time.sleep(sleep_time)
    
