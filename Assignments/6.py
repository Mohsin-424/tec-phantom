import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    
    result_label.config(text=f"Result: {result}")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
operation_var = tk.StringVar(value="+")
tk.Label(root, text="Select operation:").pack()
tk.Radiobutton(root, text="+", variable=operation_var, value="+").pack()
tk.Radiobutton(root, text="-", variable=operation_var, value="-").pack()
tk.Radiobutton(root, text="*", variable=operation_var, value="*").pack()
tk.Radiobutton(root, text="/", variable=operation_var, value="/").pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack()

# Clear button
tk.Button(root, text="Clear", command=clear).pack()

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Start the GUI loop
root.mainloop()














# ............................... GPT Response..........................................#

# import tkinter as tk
# from tkinter import messagebox

# def calculate():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         operation = operation_var.get()
        
#         if operation == "Addition":
#             result = num1 + num2
#         elif operation == "Subtraction":
#             result = num1 - num2
#         elif operation == "Multiplication":
#             result = num1 * num2
#         elif operation == "Division":
#             if num2 == 0:
#                 messagebox.showerror("Error", "Cannot divide by zero")
#                 return
#             result = num1 / num2
#         else:
#             messagebox.showerror("Error", "Please select an operation")
#             return
        
#         result_label.config(text=f"Result: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers")

# # Create the main window
# root = tk.Tk()
# root.title("Simple Calculator")

# # Create and place the widgets
# tk.Label(root, text="Enter first number:").grid(row=0, column=0)
# entry1 = tk.Entry(root)
# entry1.grid(row=0, column=1)

# tk.Label(root, text="Enter second number:").grid(row=1, column=0)
# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=1)

# tk.Label(root, text="Select operation:").grid(row=2, column=0)
# operation_var = tk.StringVar(root)
# operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
# operation_menu.grid(row=2, column=1)

# tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

# result_label = tk.Label(root, text="Result: ")
# result_label.grid(row=4, column=0, columnspan=2)

# # Start the main event loop
# root.mainloop()
