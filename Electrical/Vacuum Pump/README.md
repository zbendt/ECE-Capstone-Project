# Vacuum Pump

This vacuum pump is used to create suction in order to pick up the cultural samples. It is controlled via a relay located on the primary control PCB. The D2028 is very common among enthusiasts, and with good reason: this budget motor is dead simple, reliable, and effective. 16” of mercury over a ¼” diameter suction cup means this pump can theoretically lift a little over ⅓ of a pound, which is plenty for our application, as its load weighs only ~100 g. This allows for a safety factor of ~50%.

![VacuumPump](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/VacuumPump.jpg)
![Datasheet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/Datasheet.jpg)

## Vacuum Pump Relay

The vacuum pump simply turns on when a voltage is applied to the terminals. Therefore, the system will utilize a relay to turn the pump on and off. The schematic is as shown:

![RelayNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/RelayNet.jpg)

On the Auxiliary ATMEGA328 found on the Central PCB, the enable pin of the K1 relay is tied to PD4 (physical pin 2), which is capable of sending a 5VDC signal to open or close the relay. When the K1 relay is open, the RELAYED_VACUUM_PUMP_12V net, which is connected to the positive terminal of the vacuum pump, is left floating, meaning the vacuum pump is getting no voltage and is therefore off. When the K1 relay is closed, the RELAYED_VACUUM_PUMP_12V net receives 12VDC and turns the pump on.  

![Relay](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/Relay.jpg)

## Voltage Regulator

The 12VDC line is supplied by U1, a Cyntec MUN24AD03-SM, which is a simple buck converter that steps down a 24VDC signal to a 12VDC signal. The 24VDC signal is the “common” DC-bus throughout the system, which means it is supplied from an external load-regulating power supply that rectifies wall voltage. The Cyntec MUN24AD03-SM is capable of handling up to 3A, and is therefore more than plenty for our vacuum pump, which only draws 1A at maximum. 

![VoltageRegulator](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/VoltageRegulator.jpg)
![RegulatorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/VoltageRegulatorNet.jpg)

## Connector

The D2028 vacuum pump is connected to the Primary Control PCB via the P5 header. 

![ConnectorNet](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/ConnectorNet.jpg)
![Connector](https://github.com/Jbruslind/ECE44x_Senior_Design/blob/master/Electrical/Vacuum%20Pump/Images/Connector.jpg)
