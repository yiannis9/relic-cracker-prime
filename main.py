import threading
import tensorflow
from gui.elements import ControlsOverlay
################################################
print("Checking for GPU")
print(tensorflow.config.list_physical_devices('GPU'))

# log results to the overlay.
overlay = ControlsOverlay()
# Run the Tkinter window in a separate thread
threading.Thread(target=overlay.mainloop()).start()