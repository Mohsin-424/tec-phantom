from tkinter import ttk , Tk, PhotoImage , Canvas , filedialog

root = Tk()


ttk.Label( root , text = "This is a test label" ).pack()
canvas = Canvas( root , bg = "gray" , width = 300 , height = 400)
canvas.pack()

logo = PhotoImage( file = "1.png")
canvas.create_image( 300/2 , 400/3 , image = logo )

root.mainloop()
