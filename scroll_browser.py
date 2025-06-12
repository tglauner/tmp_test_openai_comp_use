import time
import subprocess
import pyautogui

URL = "https://www.tglauner.com/mastering_interest_rate_derivatives"

# open Google Chrome with the URL
subprocess.run(["open", "-a", "Google Chrome", URL])

# wait for the browser to load
print("Waiting for page to load...")
time.sleep(5)

# scroll down and up twice
for _ in range(2):
    pyautogui.scroll(-800)  # scroll down
    time.sleep(1)
    pyautogui.scroll(800)   # scroll up
    time.sleep(1)

print("Done scrolling.")
