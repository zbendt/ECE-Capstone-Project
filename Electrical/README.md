# Subsystem Overview

The system interacts with the samples to be tested via an end-effector that is moved by three stepper motors in a delta configuration. The goal of the Electrical Sub-System is to enable these interactions to happen at the command of the Computer Science Sub-System. The stepper motors are being controlled via an ATmega 328 microcontroller. The microcontroller is running specialized software which translates coordinates sent from a Raspberry Pi into waveforms representing the direction, distance, and speed a motor should move in. These waveforms are then passed to a stepper driver, which switches power to the motor according to the information within these waveforms. The end result is a stepper motor which can be controlled via a Raspberry Pi. An additional ATmega 328 microcontroller is utilized to control the other electrical aspects of the system as well. Such duties include enabling and disabling the vacuum pump, as well as enabling and disabling the flash for the system camera. 

## [Auxiliary Stepper Driver PCB](https://github.com/Jbruslind/ECE44x_Senior_Design/tree/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB)

![AUX_PCB](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Auxiliary%20Stepper%20Driver%20PCB/Images/PCB.jpg)

## [Central Processing PCB](https://github.com/Jbruslind/ECE44x_Senior_Design/tree/master/Electrical/Central%20Procesing%20PCB)

![Central_PCB](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Central%20Procesing%20PCB/Images/CentralPCB.jpg)

## [Vacuum Pump](https://github.com/Jbruslind/ECE44x_Senior_Design/tree/master/Electrical/Vacuum%20Pump)

![Vacuum_Pump](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/VacuumPump.jpg)
