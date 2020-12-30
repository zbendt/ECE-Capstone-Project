# Custom Delta Files
ECE 441 - 443 Project folder with files for senior capstone project for Jorian Bruslind, Mack Hall, and Zach Bendt

## Custom Delta Assembly

This model is the top level assembly for all the other models. This includes 
smaller assemblies (such as the end effector, skelton, motor node and main PCB) as well 
as standalone components (such as the Delta Arm or Motor Mount). The model has been constrained 
so that it is possible to simulate simple movement for the delta end effector (in the vertical direction). 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Custom_Delta_Assembly.png" />

### Misc Files

#### Delta Arm
The Delta Arm is functionally very simple. All that is required is that it has specific distance between the rotation point of the stepper motor and 
the pin joint of the lower arm linkage. For our application, we calculated this length to be 210mm, meaning the arm must accomate this 
distance while also being structurally stable. It is important to note that the arm must be able to maintain accuracy during movement in 
order to preserve the accuracy of the end effector. This means that the design must limit any distortion or elasitc effects of the material, for 
PLA this simply means the PLA should not bend during movement. 

The first version of the arm was a simple lever with a small cutout for the stepper collar to mount to and 2 holes for the pin and stepper motor shaft. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Delta_ArmV1.png" />

One issue that was discuess was the loss of torque in the motor due to some torque being contributed to lifting the arm itself. Since the arm has mass and 
is being rotated, this reduces the available torque made available to the end effector. To solve this issue we must reduce the overall mass of the arm. 
Using a the Autodesk Inventor "Generate Shape" tool, I was able to apply some simulated loads to the model and to remove any uncessary material while 
still maintaining the same level of stiffness/structural integrity. The resulting mesh was generated and then extruded manually into the shape shown below. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Delta_Arm.png" />

The result is a model with the same mechanical properties as the original design, but with a 60% reduction in overall material. This benefits the design 
through a faster print time as well as less mass overall in the arm. 

#### Stepper Face

The stepper face was an intersting model to try and design as it must be able to be stiff (any motor movement will contribute to small inaccuracies) and 
it must be able to hold a motor of a mass around 1kg. The result was a 3 point mounting system that was extruded to have the NEMA17 face profile. This would 
then be able to be mounted to the frame/skeleton through 2 holes on the horizontal plane and 1 on the vertical plane. The overall effect is a very stiff, rugged 
mount that is able to hold our stepper motors securely. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Stepper_Face.png" />

Another requirement of this model was that is must manipulate the stepper motor shaft so that is 60 degrees from the mounting skelton so as to create 
the "delta" robot spacing (120 degree rotation points) with 2 more translated motors. To achieve this I put holes/points where I wanted the fasteners to 
be mounted and I extruded a shape large enough for the Stepper motor (using the reference model dimensions) around those constraints. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Stepper_Face_Top.png" />

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Stepper_Face_Bot.png" />

The model was also put through stress simulations to verify that it could hold the motor weight. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Stepper_Face_sim.png" />


#### Acrylic Top

The top panels were only necessary to enclose the overall design while also providing a mounting point for the end stop limit switches. Due to the frame's 
interesting geometry I decided to go with an interlocking panel design so that there were mounting points available on the 2020 t slot extrusion for 
all the panels. As chance would have it, the maximum cut out dimensions required for these panels were the same as the side panels (so we could reuse material 
cutouts). 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Acrylic_Top.png" />

Cutouts were also made near the ends to accomodate for the 3D printed mounts that secured the 2020 aluminum.

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Custom_Delta_Assembly_Top.png" />


#### Acrylic Bot

Similarly to the top panels, the bottom panels were necessary to enclose the design while also providing mounting space for various other mechanisms. Specifically 
the bottom panels were used to load/unload samples as well as provide a mounting space for the camera and associated LED lighting. The design was made 
with the same interlocking design as the top panels with cutouts made for the 3D printed mounts. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Acrylic_Bot.png" />


#### 8020 Top Connector 

This model was made to hold 3 2020 t slot extrusion pieces 120 degrees apart so that they might be mounted to the interior of the frame. This would provide 
mounting space for the acrylic panels while also giving some much needed rigidity to the interior portion of the frame. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/8020_Top_Connector.png" />

The bottom portion of the main assembly is shown below to illustrate how these parts were used in the frame: 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Custom_Delta_Assembly_Bot.png" />


#### 8020 Bot Connector 

The bot connector is functionally the same as the top connector, it's just made a little longer due to some miscuts made during manufacturing. The T slot 
extrusion was cut a little short for this portion (due to my mismeasuring) and we had to accomate by adding some length to this part (which is why there's 
2 seperate parts)

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/8020_Bot_Connector.png" />

### Frame Skeleton 

This model is a sub assembly that creates the general skelton shape for the Delta robot. It uses 20/20 
aluminum T-slot extrusion to create a hexagon shape and is large enough to support the entire workspace 
area for the delta mechanism (as calculated by the Marginally Clever robotics Delta robot tool).  

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Frame_Skeleton.png" />

#### Acrylic Panel

The Acryic panel model was designed to be laser cut or CNC'd using typical 3 - 5 mm acrylic plates. This model was made to conform to 
the shape of the 60 deg 20/20 joint on the bottom portion of the panel and has 4 mounting holes on either side in order to provide stiffness 
to the overall frame. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Acrylic_Panel.png" />

#### Acrylic Panel Mounts

This model is the exact same as the Acrylic Panel but this was determined to be used for mounting various PCBs/main electrical elements (such as the power supply 
and Raspberry Pi). 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Acrylic_Panel_Mount.png" />


#### T-slot Extrusion (350mm, 450mm)

There isn't really anything special about these models other than it is different lengths of 20mm T slot aluminum extrusion. This was the standard 
building material we used to create the frame. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/2020_Tslot_350.png" />

The general drawing for 2020 Tslot extrusion is shown below (given in mm)

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/2020_drawing.jpg" width="300" height="300"  />


#### 60deg 20/20 Joint 

This part was a custom designed component that linked 3 T Slot extrusion profiles so that it created a 60 degree angle on the horizontal plane and a 90 degree 
angle with the vertical plane. 6 copies of this model allowed for the overall hexagon frame to take shape. This component was 3D printed using PLA material 
and was designed to withstand 4N of pushing force from either side (as shown in the simluation model) 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/60_deg_2020_joint.png" />


Simulation Model

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/60_deg_2020_joint_sim.png" />

### End Effector 

This assembly was created to help organize the end effector components. These components include the actual mechanical end effector mount, the suction cup
and nylon barb that will link the pnumatic hose. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/End_Effector_V2.png" />

#### End Effector V2

This is the actual mechanical mount model for the end effector. This was modeled after Fanuc M1ia Delta series robot end effector. The curved mounting joints 
were created so that there was an extra offset in the vertical direction (so that the end effector could read the bottom easily) and the material was shaped
so that there were strategic cutouts to preserve the structural integrity while saving material. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/End_Effector_Mech.png" />

There are M3 mounting holes surrounding the end effector plate for easy mounting of any additional components. Originally I did not know what the 
PCB to control the suction cup feedback would look like so I put as many mounting holes as I could to accomodate.  

#### Vaccum Cup and Fitting 

The Vaccum Cup was bought from McMaster and specfied to be of 1/8" NPT pipe threads and to have a specific suction capability of at least 1.0 lbs. @ 24 in. of Hg.

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Vaccum_Cup.png" />

#### Nylon Barb

The Nylon Barb model was also bought from Mcmaster to interface the 1/8" NPT pipe thread end of the suction cup to a 3mm nylon tube for the vaccum delivery. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Nylon_Barb.png" />


#### End Effector PCB

The End Effector PCB was designed to interface a laser distance sensor (the VL53L1CXV0FY) to the main PCB. This sensor must be placed in a precise location 
in order to detect when the samples are present or not below the end effector. We can use this information to detect any mis handling of the samples or 
to dynamically determine how many samples are left (by measuring the distance of the sample stack). The PCB shape was design to mimic the End effector mechanical 
design as close as possible (using the given CircuitMaker tools)

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/End_Effector_PCB.png" />

### Motor Node 

The Motor Node assembly was created to simplify the overall model organization within the main assembly. This includes the PCB model, bottom box model 
and top lid model. Overall there is nothing really special about this other than it's a case for the PCB that can be mounted onto 2020 aluminum t slot.

#### Motor Node PCB 

This model was generated through CircuitMaker's 3D modeling exporter. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Motor_Node_PCB.png" />

#### Motor Case Bottom 

This box was designed based on the connector and mounting hole placement on the PCB. What we realized during assembly is that one of the connectors on 
the opposite sides of the box (the DB9 or Ethernet) should have its top material cut away to allow for easy placement. On the box you'll notice that 
there is material bridges above each connector, one of these should be cut away (or removed entirely in the model) to actually place the populated PCB in 
the case. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Motor_Node_box.png" />

#### Motor Case Top 

The top portion of the box was modeled to have 4 mounting holes where M3 screws could secure the assmebly to itself through heatsets present in the bottom case. 
Other than that this is just a top shroud that sits on top of the box and encloses it. 

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/Motor_Node_top.png" />

### PetriFilm

PetriFilm was modeled just as a reference for the design of the system. It has been created to reflect the same color scheme and dimensions as actual Petrifilm
(specifically the anarobic bacterial film)

<img src="https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Design%20files/Delta%20Robot%20Arm/Inventor%20Files/Pictures/PetriFilm.png"  />
