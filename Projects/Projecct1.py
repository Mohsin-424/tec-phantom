from tkinter import ttk, Tk, PhotoImage, RIDGE, GROOVE, Canvas
from PIL import Image, ImageTk

class FrontEnd:
    def __init__(self, master):
        self.master = master
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        # Correct image path
        image_path = "f:/Techphantom/Projects/1.png"

        try:
            image = Image.open(image_path)
            self.logo = ImageTk.PhotoImage(image)
            ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        except FileNotFoundError:
            print(f"Image file not found: {image_path}")

        ttk.Label(self.frame_header, text="  Welcome to Image Editor Application").grid(row=0, column=1)
        ttk.Label(self.frame_header, text=" Upload, Edit and Save your images easily Here").grid(row=1, column=1)

        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))

        # Buttons
        ttk.Button(self.frame_menu, text="Upload an Image", command=self.upload_action).grid(row=0, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Crop Image", command=self.crop_action).grid(row=1, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Add Text", command=self.text_action).grid(row=2, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Draw over an image", command=self.draw_action).grid(row=3, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Blur / Smoothen", command=self.blur_action).grid(row=4, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Apply Filter", command=self.filter_action).grid(row=5, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Adjust Levels", command=self.adjust_action).grid(row=6, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Rotate", command=self.rotate_action).grid(row=7, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Flip", command=self.flip_action).grid(row=8, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="Save As", command=self.save_action).grid(row=9, column=0, padx=5, pady=5, sticky="sw")

        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()

        ttk.Button(self.apply_and_cancel, text="Apply", command=self.apply_action).grid(row=0, column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.apply_and_cancel, text="Cancel", command=self.cancel_action).grid(row=0, column=1, padx=5, pady=5, sticky="sw")
        ttk.Button(self.apply_and_cancel, text="Revert all changes", command=self.revert_action).grid(row=0, column=2, padx=5, pady=5, sticky="sw")

        # Applying Canvas to image Buttons
        self.canvas = Canvas(self.frame_menu, bg="gray", width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=10)

        # Define side_frame after refresh_side_frame method
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

        # Initial label in side_frame
        ttk.Label(self.side_frame, text="Upload an image here").grid(row=0, column=0)

    # Method to refresh side frame
    def refresh_side_frame(self):
        for widget in self.side_frame.winfo_children():
            widget.destroy()  # Remove all widgets from the side_frame

    def upload_action(self):
        self.refresh_side_frame()  # Calls the method to refresh the side frame
        ttk.Label(self.side_frame, text="Please upload an image here").grid(row=0, column=0)

    def text_action(self):
        self.refresh_side_frame()  # Calls the method to refresh the side frame
        ttk.Label(self.side_frame, text="Please enter some text").grid(row=0, column=0)

    def draw_action(self):
        pass

    def crop_action(self):
        pass

    def filter_action(self):
        pass

    def blur_action(self):
        pass

    def rotate_action(self):
        pass

    def flip_action(self):
        pass

    def save_action(self):
        pass

    def adjust_action(self):
        pass

    def apply_action(self):
        pass

    def cancel_action(self):
        pass

    def revert_action(self):
        pass

root = Tk()
FrontEnd(root)
root.mainloop()
