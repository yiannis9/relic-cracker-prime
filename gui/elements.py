import time
import tkinter as tk
from apis.wfm import WFMCaller, ModelWrapper
from logic.sampling import Sampler, Window


class ControlsOverlay(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.results_window = None
        self.attributes('-alpha', 0.3) # Set window transparency
        self.overrideredirect(1) # Remove window decorations
        self.geometry('300x100+0+0')  # Width x Height + X + Y # Set window position and size
        self.configure(bg='light green') # change color of the overlay to light green
        self.attributes('-topmost', 1) # Keep window above all others
        self.text_widgets = [] # List to store text widgets
        self.buttons = [] # List to store buttons
        self.welcome_screen()
            
    def clear_overlay(self):
        # TODO: Implement the logic to clear the overlay
        print("Clearing overlay...")
        # Store the packing options for each widget
        if not isinstance(self.results_window, type(None)):
            # for widget in self.results_window.winfo_children():
            #     widget.destroy()
            self.results_window.destroy()

    def perform_search(self):
        print("Sampling screen...")
        time_start = time.time()

        sampler = Sampler()
        sampler.sample_screen()
        img = tools.read(sampler.screenshot)

        print("Performing OCR...")
        
        model_wrapper = ModelWrapper()
        results = model_wrapper.get_results(img)
        # Clear the overlay
        self.clear_overlay()
        
        # Create a new Tkinter window for the results overlay
        self.results_window = ResultsOverlay(self, results)
        ############################################
        # move the overlay to the sampler window
        self.window = sampler.window
        print(f"Window: {self.window}, {self.window.top_left_x}, {self.window.top_left_y}, {self.window.capture_width}, {self.window.capture_height}")
        # Move and resize the results window to the position and size of the sampler window
        self.results_window.geometry(f"{self.window.capture_width}x{self.window.capture_height}+{self.window.top_left_x}+{self.window.top_left_y}")
        
        print(f"Time taken: {time.time() - time_start}")

    def welcome_screen(self):
        # -------- TEXT --------
        welcome_label = tk.Label(self, text="Welcome to Relic Cracker Prime") # Add a welcome label
        welcome_label.pack()
        self.text_widgets.append(welcome_label)
        # -------- BUTTONS --------
        quit_button = tk.Button(self, text="Quit", command=self.quit) # Add a quit button
        quit_button.pack()

        clear_button = tk.Button(self, text="Clear", command=self.clear_overlay) # Add a clear button
        clear_button.pack()

        search_button = tk.Button(self, text="Search", command=self.perform_search) # Add a search button
        search_button.pack()
        
        self.buttons.extend([quit_button, clear_button, search_button])
          
    def restore_overlay(self):
        # Pack each widget back in its original position
        for widget, options in zip(self.text_widgets + self.buttons, self.packing_options):
            widget.pack(options)
            

class ResultsOverlay(tk.Toplevel):
    def __init__(self, master, results):
        super().__init__(master)
        self.overrideredirect(1)  # Remove window decorations
        self.attributes('-alpha', 0.3)
        self.configure(bg='light green')
        self.results = results
        #add column and row weights to make the results expand to fill the window
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.display_results()
        
        
    def display_results(self):
        # Add each result to a column in the overlay
        for i, result in enumerate(self.results):
            label = tk.Label(self, text=result)
            # 4 columns, 1 row
            label.grid(row=0, column=i, sticky="nsew")
            