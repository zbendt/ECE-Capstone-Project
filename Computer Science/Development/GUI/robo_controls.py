import time
#Controls functions for the delta
sleep_time = 0.5

def turn_on_vacuum():
    print("Turning on vacuum pump")  

def pickup():
    print("Picking up sample...")
    time.sleep(sleep_time)
            
def drop():
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
    
