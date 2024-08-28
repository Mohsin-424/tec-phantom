from tkinter import ttk , Tk, PhotoImage , Canvas , filedialog
from PIL import Image , ImageTk

root = Tk()


ttk.Label( root , text = "This is a test label" ).pack()
canvas = Canvas( root , bg = "gray" , width = 300 , height = 400)
canvas.pack()

image = Image.open("Projects/1.png")

logo = ImageTk.PhotoImage( image )
canvas.create_image( 300/2 , 400/3 , image = logo )

root.mainloop()
