# ECE44x_Senior_Design
ECE 441 - 443 Project folder with files for senior capstone project for Jorian Bruslind, Mack Hall, and Zach Bendt

## Automated Microbial Analysis 

The Automated Microbial Analysis project aims to develop a system which is able to analyze a series of microbial samples on a special media 
called PetriFilm automatically. This is a 3M product that is used in a variety of scientific capacities, mainly in food science and the medical field. 

<!---![PetriFilm](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Admin_Stuff/Mechanical%20Research%20and%20Implementation/Pictures/3MPetrifilm.jpg){ width=50% }-->
<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Admin_Stuff/Mechanical%20Research%20and%20Implementation/Pictures/3MPetrifilm.jpg" width="300" height="300" />

PetriFilm is a very thin paper-like substance which has 2 layers: on one there is an agar media film that is used to grow bacterium, 
on the other there is a wax coating that is used to seal the sample from outside interference. A liquid sample can be applied to this 
agar film and left to incubate over a period of 1 - 2 days. After this time, the bacteria that were present within the sample will have 
 had enough time to grow into colonies which are visible to the human eye. These colonies can be counted and the original number of bacterium 
 per unit volume can be known from the original sample. The process to count the bacteria samples and categorize them into datasets is often 
 tedious and can take a human operator around 1 - 2 minutes per sample. With sample sizes of 50 - 60, this process 
 can easily take over an hour. The goal of our project is to use an automated system to count these bacteria colonies in sample sets of upwards 
 of 100+ in as little as 20 minutes. This data will be automatically stored and tabulated within the client's original database. 

Being a robotics project there are inherent complexities that must be resolved between subgroups such as the electrical control of the mechanical design, 
computer commands for electrical control and how effective the mechanical design facilitates the overall process. With that, the project must maintain 
a high level of communication and simplicity so that all groups are able to understand how their design affects the overall system and others designs.

### Mechanical Sub-System 

The mechanical sub-system was designed using industrial examples of delta robots in mind and special attention paid to the accuracy, speed, and cost of 
each design. Arguably, the most important aspect of our project is that is must be accurate so as not to damage the provided samples 
and to improve it's overall time cost for this process (less mistakes mean less time needed to recover). The delta robot design was made using 
many commercial off the shelf (COTS) parts with a few custom designed parts that were manufactured using a 3D printer (the Creality Ender 3 .4mm to be precise). 


<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Admin_Stuff/Mechanical%20Research%20and%20Implementation/Updated_Assembly_.png"  />

### Electrical Sub-System 

The system interacts with the samples to be tested via an end-effector that is moved by three stepper motors in a delta configuration. 
The goal of the Electrical Sub-System is to enable these interactions to happen at the command of the Computer Science Sub-System. The 
stepper motors are being controlled via an ATmega 328 microcontroller. The microcontroller is running specialized software which translates 
coordinates sent from a Raspberry Pi into waveforms representing the direction, distance, and speed a motor should move in. These waveforms 
are then passed to a stepper driver, which switches power to the motor according to the information within these waveforms. The end result is a 
stepper motor which can be controlled via a Raspberry Pi. An additional ATmega 328 microcontroller is utilized to control the other electrical aspects 
of the system as well. Such duties include enabling and disabling the vacuum pump, as well as enabling and disabling the flash for the system camera.

### Computer Science Sub-System
