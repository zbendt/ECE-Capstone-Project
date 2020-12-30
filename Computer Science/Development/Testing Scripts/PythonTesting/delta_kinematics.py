import math

#Test Values
X_VAL = 10.109
Y_VAL = -17.242
Z_VAL = -220.737
X_THETA = 0.0
Y_THETA = 0.0
Z_THETA = 0.0 

#Physical dimensions (in mm)
e = 72.0                #End triangle
f = 173.205             #Base triangle
re = 300.0              #Forearm length
rf = 210.0              #Bicept length

dps = 0.225       #degrees per step at 1/8th microstepping, 1600 steps per revolution

#Trigonometric Constants
sqrt3 = math.sqrt(3.0)
pi = 3.141592653
sin120 = sqrt3 / 2.0 
cos120 = -0.5
tan60 = sqrt3 
sin30 = 0.5
tan30 = 1/sqrt3

#Forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
#Returned status: 0=OK, -1=non-existing position

def delta_calcForward (theta1, theta2, theta3, x0, y0, z0):
    theta1 = float(theta1)
    theta2 = float(theta2)
    theta3 = float(theta3)
    x0 = float(x0)
    y0 = float(y0)
    z0 = float(z0)

    t = (f - e)*tan30/2
    dtr = pi/180.0
 
    theta1 *= dtr
    theta2 *= dtr
    theta3 *= dtr
 
    y1 = -(t + rf*math.cos(theta1))
    z1 = -rf*math.sin(theta1)
 
    y2 = (t + rf*math.cos(theta2))*sin30
    x2 = y2*tan60
    z2 = -rf*math.sin(theta2)
 
    y3 = (t + rf*math.cos(theta3))*sin30
    x3 = -y3*tan60
    z3 = -rf*math.sin(theta3)
 
    dnm = (y2 - y1)*x3 - (y3 - y1)*x2
 
    w1 = y1*y1 + z1*z1
    w2 = x2*x2 + y2*y2 + z2*z2
    w3 = x3*x3 + y3*y3 + z3*z3
     
    # x = (a1*z + b1)/dnm
    a1 = (z2 - z1)*(y3 - y1) - (z3 - z1)*(y2 - y1)
    b1 = -((w2 - w1)*(y3 - y1)-(w3 - w1)*(y2 - y1))/2.0
 
    # y = (a2*z + b2)/dnm
    a2 = -(z2 - z1)*x3 + (z3 - z1)*x2
    b2 = ((w2 - w1)*x3 - (w3 - w1)*x2)/2.0
 
    # a*z^2 + b*z + c = 0
    a = a1*a1 + a2*a2 + dnm*dnm
    b = 2*(a1*b1 + a2*(b2 - y1*dnm) - z1*dnm*dnm)
    c = (b2 - y1*dnm)*(b2 - y1*dnm) + b1*b1 + dnm*dnm*(z1*z1 - re*re)
  
    # discriminant
    d = b*b - 4.0*a*c
    if (d < 0): 
        return -1 # non-existing po
    else: 
        z0 = -0.5*(b + math.sqrt(d))/a
        x0 = (a1*z0 + b1)/dnm
        y0 = (a2*z0 + b2)/dnm
        return 0
 
 # inverse kinematics
 # helper functions, calculates angle theta1 (for YZ-pane)
def delta_calcAngleYZ(x0, y0, z0, theta, motor):
    global X_THETA
    global Y_THETA
    global Z_THETA

    theta = float(theta)
    x0 = float(x0)
    y0 = float(y0)
    z0 = float(z0)

    y1 = -0.5 * 0.57735 * f             # f/2 * tg 30
    y0 -= 0.5 * 0.57735 * e             # shift center to edge

    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 +rf*rf - re*re - y1*y1)/(2*z0)
    b = (y1-y0)/z0

    # discriminant
    d = -(a+b*y1)*(a+b*y1)+rf*(b*b*rf+rf)
    if (d < 0):
        return -1                  # non-existing point
    else:
        yj = (y1 - a*b - math.sqrt(d))/(b*b + 1)   # choosing outer po
        zj = a + b*yj
        temp = 0

        if(yj>y1):
            temp = 180.0
        else:
            temp = 0.0
        
        theta = 180.0*math.atan(-zj/(y1 - yj))/pi + temp

        if(motor == 1):
            X_THETA = float(theta)
        elif(motor == 2):
            Y_THETA = float(theta)
        elif(motor == 3):
            Z_THETA = float(theta)

    return 0
 
 # inverse kinematics: (x0, y0, z0) -> (theta1, theta2, theta3)
 # returned status: 0=OK, -1=non-existing position
def delta_calcInverse(x0, y0, z0, theta1, theta2, theta3):
    theta1 = float(theta1)
    theta2 = float(theta2)
    theta3 = float(theta3)
    x0 = float(x0)
    y0 = float(y0)
    z0 = float(z0)
    
    theta1 = theta2 = theta3 = 0
    status = delta_calcAngleYZ(x0, y0, z0, theta1, 1)
    if(status == 0): 
        status = delta_calcAngleYZ(x0*cos120 + y0*sin120, y0*cos120-x0*sin120, z0, theta2, 2)  # rotate coords to +120 deg
    if(status == 0): 
        status = delta_calcAngleYZ(x0*cos120 - y0*sin120, y0*cos120+x0*sin120, z0, theta3, 3)  # rotate coords to -120 deg
    return status

def main():
    #while(True):
    for x in range(0,1,1):
        # print("Enter x value: ")
        # X_VAL = float(input())
        # print("Enter y value: ")
        # Y_VAL = float(input())
        # print("Enter z value: ")
        # Z_VAL = float(input())
        delta_calcInverse(X_VAL, Y_VAL, Z_VAL, X_THETA, Y_THETA, Z_THETA)
        print("-----  X: " + str(X_VAL) + "  Y: "+ str(Y_VAL) + "  Z: "+ str(Z_VAL) + "  THETA1: "+ str(X_THETA) + \
             "  THETA2: "+ str(Y_THETA) + "  THETA3: " + str(Z_THETA) + "  -----")
        print(" ")

if __name__ == "__main__":
    main()