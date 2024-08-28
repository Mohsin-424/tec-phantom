from tkinter import ttk, Tk, PhotoImage

root = Tk()

ttk.Label(root, text="This is a test label").pack()
my_label_obj = ttk.Label(root, text="This is a 2nd test label")
my_label_obj.pack()

def triggered_func():
    print("Button Clicked!")

my_button_obj = ttk.Button(root, text="Click Me!", command=triggered_func).pack()

logo = PhotoImage(file = "Projects/1.png")
ttk.Label(root, image = logo).pack()
root.mainloop()
