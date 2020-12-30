# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:09:49 2020

@author: Jorian Brusind
"""
import pygame

import math

import serial
import time

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

# Open grbl serial port
s = serial.Serial('COM7',115200, timeout=.01) #COM port should be whatever the GRBL reciever is on

#____________________________Kinematics Setup_____________________________________
th1 = th2 = th3 = 90

x = y = z = 0

e = 41 #End effector radius (mm)
f = 102 #Base radius (mm)
re = 332 #Lower arm length (mm)
rf = 210 #Upper arm length (mm)

#Limits are calculated as x = -142.557 -> 142.557
# y = -142.557 -> 142.557
# z = -473.775 - -188.661

#When all motors are 0 deg then the coordinates are (0,0,-241.698)

sqrt3 = pow(3, 1/2)


sleep_t = .75

def delta_calcAngleYZ(x,y,z):
    y1 = -0.5 * .57735 * f
    y = y - (.5 * .57735 * e)
    
    a = (x*x + y*y + z*z +rf*rf - re*re - y1*y1)/(2*z);
    b = (y1-y)/z;
    
    d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf)
    if d < 0:
        return [0,-1]
    yj = (y1 - a*b - pow(d,1/2))/(b*b + 1)
    zj = a +b*yj
    
    theta = 180.0*math.atan(-zj/(y1-yj))/math.pi
    
    return theta, 0

def delta_calcInverse(x0, y0, z0):
    theta1 = theta2 = theta3 = 0
    theta1, status = delta_calcAngleYZ(x0,y0,z0)
    if status == 0:
        theta2, status = delta_calcAngleYZ(x0*math.cos(2.094) + y0*math.sin(2.094), y0*math.cos(2.094)-x0*math.sin(2.094), z0)
    if status == 0:
        theta3, status = delta_calcAngleYZ(x0*math.cos(2.094) - y0*math.sin(2.094), y0*math.cos(2.094)+x0*math.sin(2.094), z0)
        
    return theta1, theta2, theta3
#____________________________Game Controller Setup_____________________________________
    

pygame.init()

pygame.joystick.init() #Initialize the overall class that controls joysticks

clock = pygame.time.Clock()

clock.tick(20)

usb_controller = pygame.joystick.Joystick(0) #I'm gonna have a stroke reading the docs on this

#Basically you can initalize an actual "Joystick" class which has the ability to do button, axes, and trigger readings
#But for some reason the class is called "Joystick" compared to the parent class "joystick" <- wtf
#Anyway, just remember joystick -> big class, Joystick -> smaller class that has all the attributes we want

#Oh and the 0 is the id of the joystick we want (so depending on the number attached you could grab any of them)
usb_controller.init() #initialize for use

usb_axes = [0] * usb_controller.get_numaxes() #Should be 4 axes (L stick l-r up-down and R stick l-r up-down)

usb_buttons = [0] * usb_controller.get_numbuttons()

# =============================================================================
# A - 0
# B - 1
# X - 2
# Y - 3
# Left bumper - 4
# Right bumper - 5
# back button - 6
# start button - 7
# Left joystick button - 8
# right joystick button - 9
# 
# Axis 0 - Left left/right
# Axis 1 - Left up/down
# Axis 2 - L trig = 1, R trig = -1
# Axis 3 - Right up/down
# Axis 4 - Right left/right
# 
# For joysticks - bottom right make both axes positive
# =============================================================================

start_code = 0

angle1 = angle2 = angle3 = 0
step1 = step2 = step3 = 0
prevstep1 = prevstep2 = prevstep3 = 0

com1 = com2 = com3 = 0


def send_command(x,y,z):
    grbl_command = "G90 G0 " + "X" + str(x) + " Y" + str(y) + " Z" + str(z) + '\n'
    s.write(grbl_command.encode())
    print(s.readline().strip())
# Wake up grbl
s.write(str.encode("\r\n\r\n"))
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

#Let x be controlled by axis 3, y axis 4 and z axis 2
while 1:
    pygame.event.get() #VERY IMPORTANT (handles any new events) basically it updates the controller values by checking 
    #if anything changed
    
    axes = usb_controller.get_numaxes()

    for i in range(axes):
        usb_axes[i] = usb_controller.get_axis(i)
    
    buttons = usb_controller.get_numbuttons()
    
    for i in range(buttons):
        usb_buttons[i] = usb_controller.get_button(i)
    
    if usb_buttons[7] == 1:
        break
    if usb_buttons[6] == 1:
        start_code = 1
        
    if start_code:
        com1 += int(usb_axes[3]*5)
        com2 += int(usb_axes[4]*5)
        com3 += int(usb_axes[2]*5)
        com1 = clamp(com1, -130, 130)
        com2 = clamp(com2, -130, 130)
        com3 = clamp(com3, -475, -190)
        angle1, angle2, angle3 = delta_calcInverse(com1, com2, com3);
        #print(angle1, angle2, angle3)
        step1 = int(1600/360 * angle1)
        step2 = int(1600/360 * angle2)
        step3 = int(1600/360 * angle3)
        if step1 != prevstep1 or step2 != prevstep2 or step3 != prevstep3:
            grbl_command = "G90 G0 " + "X" + str(step1 * -1) + " Y" + str(step2 *-1) + " Z" + str(step3*-1) + '\n'
            print(grbl_command)
            s.write(grbl_command.encode())
            prevstep1 = step1
            prevstep2 = step2
            prevstep3 = step3
            print(s.readline().strip())
            time.sleep(.03)
#        send_command(10,-97,120)
#        time.sleep(sleep_t)
#        send_command(-152,-65,145)
#        time.sleep(sleep_t)
#        send_command(-111,146,-72)
#        time.sleep(sleep_t)
#        send_command(43,102,-111)
#        time.sleep(sleep_t)
#        send_command(117,-76,10)
#        time.sleep(sleep_t)
#        send_command(21,52,45)
#        time.sleep(sleep_t)
#        send_command(-29,-3,-9)
#        time.sleep(sleep_t)
#        send_command(51,86,79)
#        time.sleep(sleep_t)
#        send_command(-29,-3,-9)
#        time.sleep(sleep_t * 10)
        
s.close()
        
    
    