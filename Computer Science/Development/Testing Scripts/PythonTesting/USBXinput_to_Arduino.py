import pygame
import serial

try:
    ser = serial.Serial('COM5', 115200, timeout = 3, parity = serial.PARITY_NONE)
    pygame.init()
    pygame.joystick.init()
    while(1):
        pygame.event.pump()
        control_list = []
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()            
            name = joystick.get_name()
            axes = joystick.get_numaxes()       
            #print(axes)
            for i in range(axes):
                control_list.append("{:.2f}".format(joystick.get_axis(i) + 1))                
            buttons = joystick.get_numbuttons()
            #print(buttons)
            for i in range(buttons):
                control_list.append("{:.2f}".format(joystick.get_button(i)))
            for i in range(len(control_list)):
                #print(bytes(control_list[i], 'utf8'))
                #print(len(control_list))
                ser.write(bytes(control_list[i], 'utf8'))
            ser.write(bytes("!", 'utf8'))
        print(ser.read(100))
finally:
    ser.close()
    print("finish")