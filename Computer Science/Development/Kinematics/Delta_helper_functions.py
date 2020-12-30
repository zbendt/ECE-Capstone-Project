# -*- coding: utf-8 -*-
"""
Created on Wed May  6 11:04:10 2020

@author: Jorian Bruslind
"""

import math

th1 = th2 = th3 = 90

x = y = z = 0

e = 45 #End effector radius (mm)
f = 60 #Base radius (mm)
re = 300 #Lower arm length (mm)
rf = 210 #Upper arm length (mm)

sqrt3 = pow(3, 1/2)



def delta_calcAngleYZ(x,y,z):
    print(x,y,z)
    y1 = -0.5 * .57735 * f
    y = y - (.5 * .57735 * e)
    
    a = (x*x + y*y + z*z +rf*rf - re*re - y1*y1)/(2*z);
    b = (y1-y)/z;
    
    d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf)
    print(a,b,d)
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
        print(x0,y0,z0)
        theta2, status = delta_calcAngleYZ(x0*math.cos(2.094) + y0*math.sin(2.094), y0*math.cos(2.094)-x0*math.sin(2.094), z0)
    if status == 0:
        print(x0,y0,z0)
        theta3, status = delta_calcAngleYZ(x0*math.cos(2.094) - y0*math.sin(2.094), y0*math.cos(2.094)+x0*math.sin(2.094), z0)
        
    return theta1, theta2, theta3

print(delta_calcInverse(72,-72,-200))