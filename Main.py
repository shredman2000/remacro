import pygame
import keyboard
import time
import json

pygame.init()
pygame.joystick.init()

controller = pygame.joystick.Joystick(0)
controller.init()

recording = False
recorded = []
start_time = None
last_f8 = False

def clean_axis(a):
    if abs(a) < 0.00:
        return 0.0
    return a

while True:

    pygame.event.pump()

    # F8 toggle
    f8 = keyboard.is_pressed("f8")

    if f8 and not last_f8:
        if not recording:
            print("Recording...")
            recording = True
            recorded = []
            start_time = time.perf_counter()
        else:
            print("Saving...")
            recording = False

            with open("macro.json", "w") as f:
                json.dump(recorded, f)

            print(f"Saved {len(recorded)} frames")

    last_f8 = f8


    if recording:

        axes = [clean_axis(controller.get_axis(i)) for i in range(controller.get_numaxes())]
        buttons = [controller.get_button(i) for i in range(controller.get_numbuttons())]
        hats = [controller.get_hat(i) for i in range(controller.get_numhats())]

        recorded.append({
            "time": time.perf_counter() - start_time,
            "axes": axes,
            "buttons": buttons,
            "hats": hats
        })

    time.sleep(0.001)  