# Stepper Driver PCB

This PCB acts as a link between the Primary Control PCB and the stepper motors themselves. Since there are three stepper motors, there will be three separate instances of this PCB in the final system. This PCB takes in a signal from one of the ATMEGA328s on the Primary Control PCB, and outputs another electrical signal which will turn the stepper motors. In order to verify that this PCB is working correctly, there are status LEDs for 24V and 5V power, as well as status LEDs for RX and TX packets.

![PCB](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/PCB.jpg)
![PCB_Bottom](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/PCB_Bottom.jpg)
![PCB_LayerTop](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/PCB_LayerTop.jpg)
![PCB_LayerBottom](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/PCB_LayerBottom.jpg)

## Ethernet Port

The Auxiliary Driver PCB accepts its input from the Central Processing PCBs in the form of an ethernet cable. The ethernet cable carries 24VDC, a direction signal, a step signal, and RX and TX lines for serial communication. The ethernet cable was chosen due to its ubiquity and low cost. Four pins in total are dedicated to power delivery, while the other four pins are dedicated to other signals.

![EthernetNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/EthernetNet.jpg)
![Ethernet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/EthernetNet.jpg)

## Stepper Motor Connection

J2, a Phoenix Contact 1803293, is the connector for the stepper motor itself. The connector is compatible with the stepper motors we already had as a group, and were chosen as a result. This connector is capable of handling up to 8A. Since the motors themselves only use up to 2A maximum at a time, this has a safety factor of 400%. 

![MotorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/MotorNet.jpg)
![Motor](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/Motor.jpg)

## Encoder Connector and Signal Processing

J3, a TE Connectivity / AMP 5747844-4, is the DB9 connector used to interface with the encoder integrated on the stepper motor itself. The DB9 connector allows the encoder signal to be read in by the ATtiny85 (U2 on the PCB), where the signal is interpreted. Finally, the motor position is sent back to the Central Processing PCB along the ethernet cable via serial communication. This allows the software to know where the motors are physically at all times. This allows a greater degree of control, because the motors may occasionally “miss” a step and become misaligned with their intended position. The encoder signal allows us to detect this and either compensate for this error on the software side of things or completely re-home the system altogether. Missing a step typically only occurs at higher speeds, and our motors are run at relatively low speeds, so it should not come up too often, but it is always good to prepare for the worst. 

![Attiny85](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/ATtiny85.jpg)
![DB9_Net](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/DB9_Net.jpg)
![ATtiny85_and_DB9](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/ATtiny85_and_DB9.jpg)

## Voltage Regulation

X1 is a Texas Instruments LMZM23601V5SILT buck converter which converts the 24VDC line to a 5VDC line for use on the Auxiliary Driver PCB. The 5V line is used to power the stepper driver, the encoder, the Attiny85, and the RX, TX, and 5V status LEDs. The LMZM23601V5SILT is rated for up to 1A of use, but the auxiliary current the Auxiliary Driver PCB draws is much less than that in reality.

![VoltageRegulatorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/VoltageRegulatorNet.jpg)
![VoltageRegulator](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/VoltageRegulator.jpg)

## Stepper Drivers

J8-L and J8-R are sockets for where a stepper driver daughterboard (a.k.a. stepstick) could connect. Although it can be used for testing and debugging purposes, this socket is not to be  used in the final system, as all microcontrollers under 64 pins must be soldered directly on the PCB. On the opposite side of the PCB, there is a place to solder an SMD stepper driver chip (U1 on the PCB). We chose to go with the Trinamic TMC2209 due to its low cost and high reliability. The TMC2209 is capable of handling up to 2.2 A per stepper motor, which is below our peak of 2 A. The stepper driver will have a heatsink in addition in order to help dissipate heat and ensure high performance over extended operational periods. 

![StepperDriverNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/ArduinoSocketNet.jpg)
![StepperDriverSocket](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/ArduinoSocket.jpg)
![TMC2209](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/Microcontroller.jpg)

