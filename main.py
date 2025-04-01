import streamlit as st
import pyautogui
import time
import random
import threading
import os
import signal

# Variables to control the movement
running = False
moving_thread = None

def switch_screens():
    max_switches = random.randint(1, 5)
    pyautogui.keyDown('alt')
    for _ in range(1, max_switches):
        pyautogui.press('tab')
    pyautogui.keyUp('alt')

def wiggle_mouse():
    max_wiggles = random.randint(4, 9)
    for _ in range(1, max_wiggles):
        coords = get_random_coords()
        pyautogui.moveTo(x=coords[0], y=coords[1], duration=5)
        time.sleep(10)

def get_random_coords():
    screen = pyautogui.size()
    width = screen[0]
    height = screen[1]
    return [random.randint(100, width - 200), random.randint(100, height - 200)]

def run_script():
    global running
    while running:
        switch_screens()
        wiggle_mouse()
        time.sleep(1)

def start_script():
    global running, moving_thread
    if not running:
        running = True
        moving_thread = threading.Thread(target=run_script)
        moving_thread.start()

def stop_script():
    global running
    running = False
    # Terminate the Streamlit server process
    os.kill(os.getpid(), signal.SIGTERM)

# Streamlit App
st.title('Mouse and Screen Controller')

start_button = st.button('Start')
stop_button = st.button('Stop')

if start_button:
    start_script()
    st.success("Script started!")

if stop_button:
    stop_script()
    st.success("Script stopped!")