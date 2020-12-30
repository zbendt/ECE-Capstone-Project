import grblProofOfConcept
import time

DELAY_TIME = .05
SIZE = 8
CONT_MAT0 = ["" for x in range(SIZE)]
CONT_MAT1 = ["x0y0z0","x1y1z1","x0y0z0"]
CONT_MAT2 = ["x-.5y.5z.5","x0y0z0","x.5y.5z-.5","x0y0z0","x.5y-.5z.5","x0y0z0","x1y1z1","x0y0z0"]
CONT_MAT3 = ["$$"]

def manual_mode():
    grblCom0 = grblProofOfConcept.ArduinoSerialObj("COM3")
    while(True):
        for x in range(0,SIZE,1):
            print("Enter x: ")
            x_val = "x"+ str(input())
            print("Enter y: ")
            y_val = "y"+ str(input())
            print("Enter z: ")
            z_val = "z"+ str(input())
            cmd_str = x_val + y_val + z_val
            CONT_MAT0[x] = cmd_str
            print("--cmd_str" + str(x) + ": " + CONT_MAT0[x])
            grblCom0.write(CONT_MAT0[x])
            time.sleep(DELAY_TIME)

def run_program1():
    grblCom1 = grblProofOfConcept.ArduinoSerialObj("COM3")
    for x in range(0, SIZE, 1):
        grblCom1.write(CONT_MAT1[x])
        time.sleep(DELAY_TIME)

def run_program2():
    grblCom2 = grblProofOfConcept.ArduinoSerialObj("COM3")
    for x in range(0, SIZE, 1):
        grblCom2.write(CONT_MAT2[x])
        time.sleep(DELAY_TIME)

def run_program3():
    grblCom3 = grblProofOfConcept.ArduinoSerialObj("COM3")
    for x in range(0, SIZE, 1):
        grblCom3.write(CONT_MAT3[x])
        time.sleep(DELAY_TIME)

def main():
    print("Enter Program Number: ")
    program = int(input())

    if(program == 0):
        manual_mode()

    if(program == 1):
        run_program1()

    if(program == 2):
        run_program2()

    if(program == 3):
        run_program3()

    else:
        print("--------End of Program---------")

if __name__ == "__main__":
    main()