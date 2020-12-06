import time, numpy as np, pyautogui, imageio
from PIL import Image

t0 = time.time()
with imageio.get_writer('test.gif', mode='I', duration=0.1) as writer:
    while True:
        t1 = time.time()
        img = pyautogui.screenshot(region=(0,0,1920,1080))
        img = img.resize((1920, 1080),Image.ANTIALIAS)
        writer.append_data(np.array(img))
        t2 = time.time()
        time.sleep(0.5 - (t2 - t1))
        if t2 - t0 > 6:
            break
