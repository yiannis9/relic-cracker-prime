'''
This file is responsible for handling the hotkeys.
'''
import sys
import time
import threading

from pynput.keyboard import Listener, Key, KeyCode
from keras_ocr import pipeline, tools
from logic.sampling import Sampler
from gui.elements import Overlay


def get_vk(key):
    """
    Get the virtual key code from a key.
    These are used so case/shift modifications are ignored.
    """
    return key.vk if hasattr(key, 'vk') else key.value.vk


def on_press(key):
    """ When a key is pressed """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in combination_to_function:  # Loop through each combination
        if is_combination_pressed(combination):  # Check if all keys in the combination are pressed
            combination_to_function[combination]()  # If so, execute the function


def on_release(key):
    """ When a key is released """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys


def is_combination_pressed(combination):
    """ Check if a combination is satisfied using the keys pressed in pressed_vks """
    return all([get_vk(key) in pressed_vks for key in combination])


def ctrl_shift_s():
    # Your OCR logic here (capture screenshot, perform OCR, etc.)
    print("Sampling screen...")
    start = time.time()

    sampler = Sampler()
    sampler.sample_screen()
    # img = tools.read(sampler.screenshot)

    # print("Performing OCR...")
    # # Perform OCR on the image
    # results = pipeline.recognize([img])

    # print("Results:")
    # # Loop through the results and print the detected text and bounding boxes
    # for result in results:
    #     print(result)

    # log results to the overlay.
    overlay = Overlay()
    # Run the Tkinter window in a separate thread
    #TODO: fix this so that i can still run hotkeys while overlay is on
    threading.Thread(target=overlay.mainloop()).start()

    print(f"Time taken: {time.time() - start}")
    
    
def ctrl_shift_q():
    print("Exiting...")
    raise SystemExit


def ctrl_shift_c():
    print("Clearing the screen")
    # Your logic here to clear the screen
    # ...    
    

# The currently active modifiers
pressed_vks = set()
# The key combination to check
combination_to_function = {
    frozenset([KeyCode(vk=162), KeyCode(vk=160), KeyCode(vk=67)]) : ctrl_shift_c, # Ctrl + Shift + c
    frozenset([KeyCode(vk=162), KeyCode(vk=160), KeyCode(vk=83)]) : ctrl_shift_s, # Ctrl + Shift + s
    frozenset([KeyCode(vk=162), KeyCode(vk=160), KeyCode(vk=81)]) : ctrl_shift_q, # Ctrl + Shift + q
}