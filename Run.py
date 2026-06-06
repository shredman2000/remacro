import vgamepad as vg
import json
import time
import keyboard

def clamp(a):
    if abs(a) < 0.00:
        return 0.0
    return max(-1.0, min(1.0, a))

with open("macro.json", "r") as f:
    macro = json.load(f)

gamepad = vg.VX360Gamepad()

print("Press F9 to start replay...")
keyboard.wait("f9")

print("Starting in 3 seconds...")
time.sleep(3)

start = time.perf_counter()
i = 0
n = len(macro)

while i < n:

    now = time.perf_counter() - start


    while i < n - 1 and macro[i + 1]["time"] <= now:
        i += 1

    frame = macro[i]

    axes = frame["axes"]
    buttons = frame["buttons"]

    # --- STICKS ---
    gamepad.left_joystick_float(
        x_value_float=clamp(axes[0]),
        y_value_float=clamp(axes[1])
    )

    gamepad.right_joystick_float(
        x_value_float=axes[2],
        y_value_float=axes[3]
    )

    # --- TRIGGERS ---
    lt = (axes[4] + 1) / 2
    rt = (axes[5] + 1) / 2

    gamepad.left_trigger_float(lt)
    gamepad.right_trigger_float(rt)

    # --- BUTTONS ---
    if buttons[0]:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

    if buttons[1]:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    if buttons[2]:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

    if buttons[3]:
        gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
    else:
        gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

    gamepad.update()

    time.sleep(0.001)