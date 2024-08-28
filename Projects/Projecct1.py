from tkinter import ttk , Tk , PhotoImage , Canvas , filedialog 

root = Tk()


# filename = filedialog.askopenfilename()
filename = filedialog.asksaveasfile()
print(filename)
root.mainloop()
