#	PCB Files

This directory contains all of the PCB related files for manufacturing, documentation, and 3D modeling. All of these files were generated using CircuitMaker's built-in "generate outputs" function, which allows for the generation of schematics, PCB print files, 3D Step files, and Gerber files (for PCB manufacturing). 

The layout for the subdirectories is fairly simple. Within each main file there contains a list of outputs ordered as: 

## BOM

This is a generated Bill of Materials (BOM) that contains a list of all the CircuitMaker components used. This can sometimes not be very accurate due to the fact that crosslisting actual components with the built in CircuitMaker libaries can be difficult. Sometimes the various passive components used could be different values or different types. For example, we may reuse a 20uF capacitor model, but change the value to 10uF. The reason being is that it would take up too much time to individually go through all the components, footprints, and specifications for each component and source them through digikey or some other distributor. Instead, we know what we need and we just quickly put something that's the same footprint/type on the schematic and sort out the details later. The ICs or other more specific parts are almost always sourced directly however (so any chips or specialized component can be trusted, just not simple passives)  

In the end we kinda shoot ourselves in the foot for documentation purposes later, but the time saved makes it worth it (for the most part). Just a heads-up if anyone uses these files later, the actual components should be taken with a grain of salt. 

## ExportSTEP

Luckily for our mechanical designer, CircuitMaker has a built in function that will export a STEP file of the circuit board that is populated with all the components in the exact positions they're in (so long as the components are matched with a 3D model within the CircuitMaker library). 

This directory contains that exported step (and a generated .ipt version for our own modeling purposes).   

## Geber

PCB Manufacturers need a specialized set of files in order to actually manufacture the PCBs. One such set of files are called "Gerber Files". These contain the layer information for the specific circuit board such as the copper placement on the top/bottom or middle layers (depending on how many layers are present) as well as information on the hole placement, where soldermask should/shouldn't be placed, where the outline of the board is, where any board cutouts should be. Here's a brief description of each file type: 

- .GBL - Gerber Bottom Layer (copper placement on bottom layer)
- .GBO - Gerber Bottom Overlay (the text overlay on the bottom layer)
- .GBS - Gerber Bottom Solder (where the bottom solder mask should be placed)
- .GPB - Gerber Bottom Paste (where solder paste should be - almost never used by us) 
- .GTL - Gerber Top Layer (copper placement on top layer)
- .GTO - Gerber Top Overlay (the text overlay on the top layer)
- .GTS - Gerber Top Solder (where the top solder mask should be placed)
- .GTB - Gerber Top Paste (where solder paste should be - almost never used by us) 
- .GKO - Gerber Keep Out (what the PCB manufacturer's shouldn't touch - we use this as an outline for our board) 


Everything else pretty much isn't used by us. 

## Manufacturing Files 

These contain all the files that we *actually* need to manufacture the PCB (what we send to the factory). 

- .GBL
- .GBO
- .GBS
- .GTL
- .GTO
- .GTS
- .GKO
- .XLN - This is a special file for drilling

In this directory you'll find all these files and a .zip folder containing them which you can use to send to a factory for PCB manufacture. 

## NC Drill

This directory has the drilling outputs for the specific PCB. This will include information on what hole should be placed and where. There is a specific file in here that usually has the structure "projectname.txt", this file has all the CNC commands to actually route the holes for the board. We take this file, rename the extension .XLN and combine it with our other gerber's for manufacture (not sure why, we've just always done it and it works) 

## *"projectname".pdf* 

This pdf has all the information about the circuit board such as schematics and PCB layout. You can find all the details about the specific project in this. 


