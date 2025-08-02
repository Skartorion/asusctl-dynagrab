import subprocess
import time
import numpy as np
from mss import mss

def set_keyboard_color(rgb_hex):
    subprocess.run(
        ["asusctl", "aura", "static", "-c", rgb_hex],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

def get_screen_average_color():
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = np.array(screenshot)
        avg = img[:, :, :3].mean(axis=(0, 1))
        return "{:02x}{:02x}{:02x}".format(int(avg[0]), int(avg[1]), int(avg[2]))

def main():
    last_color = None
    while True:
        color = get_screen_average_color()
        if color != last_color:
            set_keyboard_color(color)
            last_color = color
        time.sleep(0.25)

if __name__ == "__main__":
    main()
