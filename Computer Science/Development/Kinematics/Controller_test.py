import pygame

pygame.init()

pygame.joystick.init() #Initialize the overall class that controls joysticks

clock = pygame.time.Clock()

clock.tick(20)

print(pygame.joystick.get_count()) #Print the number of joysticks currently found on this machine

usb_controller = pygame.joystick.Joystick(0) #I'm gonna have a stroke reading the docs on this

#Basically you can initalize an actual "Joystick" class which has the ability to do button, axes, and trigger readings
#But for some reason the class is called "Joystick" compared to the parent class "joystick" <- wtf
#Anyway, just remember joystick -> big class, Joystick -> smaller class that has all the attributes we want

#Oh and the 0 is the id of the joystick we want (so depending on the number attached you could grab any of them)
usb_controller.init() #initialize for use

usb_axes = [0] * usb_controller.get_numaxes() #Should be 4 axes (L stick l-r up-down and R stick l-r up-down)

usb_buttons = [0] * usb_controller.get_numbuttons()

# =============================================================================
# A - 0
# B - 1
# X - 2
# Y - 3
# Left bumper - 4
# Right bumper - 5
# back button - 6
# start button - 7
# Left joystick button - 8
# right joystick button - 9
# 
# Axis 0 - Left left/right
# Axis 1 - Left up/down
# Axis 2 - L trig = 1, R trig = -1
# Axis 3 - Right up/down
# Axis 4 - Right left/right
# 
# For joysticks - bottom right make both axes positive
# =============================================================================



while 1:
    pygame.event.get()
    
    #print(usb_controller.get_numaxes())
    
    #print(usb_controller.get_name())
    
    axes = usb_controller.get_numaxes()

    for i in range(axes):
        usb_axes[i] = usb_controller.get_axis(i)
    
    buttons = usb_controller.get_numbuttons()
    for i in range(buttons):
        usb_buttons[i] = usb_controller.get_button(i)
   
    print(usb_buttons)

    print(usb_axes) 
    
    if usb_buttons[0] == 1:
        break

pygame.joystick.quit()