# GRBL Code

This project utilizes [GRBL](https://github.com/grbl/grbl), which is an open-source stepper motor driver controller designed to run natively on an Arduino Uno. However, the Arduino Nano has the same number of digital output pins as the Arduino Uno, so it is possible to modify the code to run on the Nano.

The Arduino Nano barely has enough memory to flash grbl on to it, but it does. From there, the cpu_map.h file needs to be modified, in order to redirect the output signals to the proper pins. For our case, the signals were redirected to the following pins:

[GrblNanoPinout](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Code/GRBL%20Code/GrblNanoPinout.PNG)

Every other part of grbl is unmodified, aside from a few grbl settings used for smoother operation. Such settings are set as follows:

|Setting|Value|
|----|----|
|$0|10|
|$1|255|
|$2|0|
|$3|7|
|$4|0|
|$5|0|
|$6|0|
|$10|1|
|$11|0.010|
|$12|0.002|
|$13|0|
|$20|0|
|$21|0|
|$22|0|
|$23|0|
|$24|25.000|
|$25|500.000|
|$26|250|
|$27|1.000|
|$30|1000|
|$31|0|
|$32|0|
|$100|250.000|
|$101|250.000|
|$102|250.000|
|$110|500.000|
|$111|500.000|
|$112|500.000|
|$120|10.000|
|$121|10.000|
|$122|10.000|
|$130|300.000|
|$131|300.000|
|$132|300.000|

Since both the Arduino Uno and Arduino Nano utilize the ATmega 328 microcontroller, that was a large determining factor as to why we chose it to use it for this project.
