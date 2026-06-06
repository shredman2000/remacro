import pygame
import time

pygame.init()
pygame.joystick.init()

c = pygame.joystick.Joystick(0)
c.init()

print("Move ONLY RT slowly")

while True:
    pygame.event.pump()

    for i in range(c.get_numaxes()):
        print(i, round(c.get_axis(i), 3), end=" | ")

    print()
    time.sleep(0.1)