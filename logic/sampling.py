from dataclasses import dataclass
from PIL import ImageGrab
from PIL import Image
from datetime import datetime
from screeninfo import get_monitors
import cv2
import numpy as np


@dataclass
class Window:
    top_left_x: int
    top_left_y: int
    capture_width: int
    capture_height: int
    

class Sampler:
    def __init__(self) -> None:
        # Get screen resolution
        # primary monitor should be 0
        self.screen_width = get_monitors()[0].width
        self.screen_height = get_monitors()[0].height
        self.window = None
        print(f"Primary Monitor Screen resolution: {self.screen_width}x{self.screen_height}")
    
    def sample_screen(self, image=None):

        # Define a desired capture area size (adjust as needed)
        capture_width = int(self.screen_width * 2 / 3 )  # Adjust width for your desired capture size
        capture_height = int(self.screen_height / 4 )  # Adjust height for your desired capture size
        middle_x = int(self.screen_width / 2)
        middle_y = int(self.screen_height / 2)
        top_left_x = middle_x - int(capture_width / 2)
        top_left_y = middle_y - int(capture_height / 2)

        self.window = Window(top_left_x, top_left_y, capture_width, capture_height)

        print("No image provided")
        # Capture the screenshot
        self.screenshot = ImageGrab.grab((top_left_x, top_left_y, top_left_x + capture_width, top_left_y + capture_height))
        
    def from_file(self, image=None):
        img  = f'./test_data/y46BWpd.png'
        # img  = f'./test_data/230410_screenshots_20190707004456_1.jpg'
        # img  = f'./test_data/ezgif-4-36a00c1e29.jpg'
        img = np.array(Image.open(img))
        print(img.shape)
        
        # check if img is np array
        if not isinstance(img, type(None)):
            print("Drawing rectangle on image")
            capture_width = int(img.shape[1] *2 / 3 )
            capture_height = int(img.shape[0] / 4)
            middle_x = int(img.shape[1] / 2)
            middle_y = int(img.shape[0] / 2)
            # Calculate top-left corner coordinates for centered capture
            top_left_x = middle_x - int(capture_width /2)
            top_left_y = middle_y - int(capture_height /2) - int(middle_y/3)
            
            self.window = Window(top_left_x, top_left_y, capture_width, capture_height)
            w = self.window
            img_copy = img.copy()
            img_copy = cv2.rectangle(img_copy,
                                     (w.top_left_x, w.top_left_y),
                                     (w.top_left_x + w.capture_width, w.top_left_y + w.capture_height),
                                     color=(0, 0, 255),
                                     thickness=2)
            # cv2.imshow('img', img_copy)
            # cv2.waitKey(0)
            self.screenshot = img[w.top_left_y:w.top_left_y+w.capture_height, w.top_left_x:w.top_left_x+w.capture_width]
        
    def save_ss(self):
        self.screenshot.save(f'ss_{datetime.now()}')

