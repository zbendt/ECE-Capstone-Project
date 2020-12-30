import delta_kinematics

X_VAL = 10.109
Y_VAL = -17.242
Z_VAL = -220.737

X_THETA = 0.0
Y_THETA = 0.0
Z_THETA = 0.0

def main():
    while(True):
        # print("Enter x value: ")
        # X_VAL = float(input())
        # print("Enter y value: ")
        # Y_VAL = float(input())
        # print("Enter z value: ")
        # Z_VAL = float(input())

        delta_kinematics.delta_calcInverse(X_VAL, Y_VAL, Z_VAL, X_THETA, Y_THETA, Z_THETA)

        print("-----  X: " + str(X_VAL) + "  Y: "+ str(Y_VAL) + "  Z: "+ str(Z_VAL) + "  THETA1: "+ str(X_THETA) + \
             "  THETA2: "+ str(Y_THETA) + "  THETA3: " + str(Z_THETA) + "  -----")
        print(" ")

if __name__ == "__main__":
    main()
