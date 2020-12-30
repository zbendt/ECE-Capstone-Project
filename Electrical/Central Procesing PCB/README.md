# Central Processing PCB

This PCB handles everything related to driving the motors from a software point of view. It interprets the motor coordinates sent from the Raspberry Pi, sends signals and power to the Auxiliary PCBs, and processes encoder data from the motors. 

![CentralPCB](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/CentralPCB.jpg)
![CentralPCBBottom](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/CentralPCB_Bottom.jpg)
![PCB_TopLayer](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/PCB_TopLayer.jpg)
![PCB_BottomLayer](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/PCB_BottomLayer.jpg)

## Ethernet Connectors

The Auxiliary Driver PCB accepts its input from the Central Processing PCBs in the form of an ethernet cable. The ethernet cable carries 24VDC, a direction signal, a step signal, and RX and TX lines for serial communication. The ethernet cable was chosen due to its ubiquity and low cost. Four pins in total are dedicated to power delivery, while the other four pins are dedicated to other signals. Since the Central Processing PCB has to control three separate Auxiliary Diver PCBs, the Central board has three ethernet ports (J3, J4, & J5), one for each Auxiliary PCB. 

![EthernetNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/EthernetNet.jpg)
![Ethernet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/Ethernet.jpg)

## Power Conversion and Distribution

The Central Processing PCB distributes power to the rest of the system from the external power supply. The board takes in power from J0, a male XT30 connector, which is rated up to 30A as the name implies. The power supply itself that we are using is rated for only 20A, so this is a non-issue. 

![ConNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/ConnectorNet.jpg)
![Connector](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/Connector.jpg)

The Central Processing PCB also requires a fairly robust 5VDC converter, since it is responsible for powering the Raspberry Pi as well as two ATMEGA328 microcontrollers. As such, the PCB utilizes the Bel Fuse SRBH-06H1A1R (U3 on the PCB \[missing a 3D model]), which is capable of stepping down a 24VDC input into a 5VDC output up to 6A. This is overkill for our system, as each of the listed components that draw from the SRBH-06H1A1R only take about 1A each. As such, we have a safety factor of 100%.

![RegulatorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/RegulatorNet.jpg)
![Regulator](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/Regulator.jpg)

As mentioned above, the Central PCB provides 5VDC to the Raspberry Pi via its GPIO pins. This is not recommended by the makers of the Raspberry Pi, as the GPIO pins bypass the internal fusing and regulation done in order to ensure a safe and regulated 5V line for the system. Before going to the upside-down headers that allow the Central PCB to be worn as a Raspberry Pi hat, the 5V line on the Central PCB must go through a resettable thermal fuse (F1 on the PCB) in order to ensure that the Raspberry Pi cannot draw enough current to harm itself. The fuse we are using is the Bel Fuse 0ZCH0200FF2E, which is rated for 2A before tripping. Once tripped, the fuse will reset after being returned to room temperature.

![RPiNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/RPiNet.jpg)
![RPi](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/RPi.jpg)

Furthermore, the Central PCB is also responsible for providing 12VDC to drive the vacuum pump. The vacuum pump simply turns on when a voltage is applied to the terminals. Therefore, the system will utilize a relay to turn the pump on and off. The schematic is as shown:

![RegulatorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/VoltageRegulatorNet.jpg)

The 12VDC line is supplied by U1, a Cyntec MUN24AD03-SM, which is a simple buck converter that steps down a 24VDC signal to a 12VDC signal. The 24VDC signal is the “common” DC-bus throughout the system, which means it is supplied from an external load-regulating power supply that rectifies wall voltage. The Cyntec MUN24AD03-SM is capable of handling up to 3A, and is therefore more than plenty for our vacuum pump, which only draws 1A at maximum. 

![VoltageRegulator](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/VoltageRegulator.jpg)

## Vacuum Pump

On the Auxiliary ATmega 328 found on the Central PCB, the enable pin of the K1 relay is tied to PD4 (physical pin 2), which is capable of sending a 5VDC signal to open or close the relay. When the K1 relay is open, the RELAYED_VACUUM_PUMP_12V net, which is connected to the positive terminal of the vacuum pump, is left floating, meaning the vacuum pump is getting no voltage and is therefore off. When the K1 relay is closed, the RELAYED_VACUUM_PUMP_12V net receives 12VDC and turns the pump on.  

![Relay](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/Relay.jpg)

The D2028 vacuum pump is connected to the Primary Control PCB via the P5 header. 

![ConnectorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/ConnectorNet.jpg)
![Connector](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/Connector.jpg)

## Camera Flash

The K2 relay is responsible for enabling the LEDs below the camera, in order to act as a flash. These LEDs take a 5V input, and are therefore tied to the 5V regulated line on the board. This setup is very similar to the vacuum pump, however it is only 5VDC instead of 12VDC. 

![FlashRelayNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/FlashRelayNet.jpg)
![FlashRelay](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/FlashRelay.jpg)

## Onboard Microcontrollers

The Central PCB also needs to connect all of the prior connections to two ATmega 328 microcontrollers, which will actually run the software we need to control the system. The PCB includes sockets to plop in two Arduino Nanos for testing and debugging purposes, but this will not be used in the final system. The back of the PCB hides the solder pads for two SMD ATmega 328s (AUX_ and Stepper_ on the PCB), as well as two external 16MHz clocks (X1 and X2), and two 5V regulators (Q1 and Q2).

![ArduinoA](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/Arduino_A.jpg)
![ArduinoB](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/Arduino_B.jpg)
![ArduinoC](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/Arduino_C.jpg)

Essentially, the PCB has the equivalent hardware of two integrated Arduino Nanos on board. They have the equivalent connections lifted straight from the official Nano schematic itself found [here](https://www.arduino.cc/en/uploads/Main/Arduino_Nano-Rev3.2-SCH.pdf).

The Stepper_ ATMEGA 328 is responsible for running a program called ‘grbl’. grbl is a well-established software that is used for driving stepper motors. The user inputs G-Code, and grbl will generate the equivalent signals to be sent to the stepper motor driver that will move the motor to the coordinates defined in said G-Code. Essentially, the stepper driver is a median in which grbl can move the stepper motor directly. Along with other signals, the necessary signals generated from grbl are sent through the ethernet cable, where they are eventually interpreted by the TCM2209 on the Auxiliary Diver PCB. In the final system, the Raspberry Pi will be running a script which will send G-Code serially to the Stepper_ ATMEGA, which will control the position of the stepper motors indirectly via the stepper motor divers. 

The AUX_ ATMEGA 328 is responsible for reading back the messages sent by the Auxiliary Stepper PCBs, as well as turning on the relays for the vacuum pump and the camera flash. An additional ATMEGA 328 was used in conjunction with the Stepper_ ATMEGA 328 due to computational bottlenecks. grbl is a very demanding program, and attempting to run additional code could impact the timing of the wave generation, meaning that the end stepper motor motion would not be as accurate or as smooth.
