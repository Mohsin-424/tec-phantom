import tkinter as tk

# Define the Car class for sale and rent
class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"

# Define the Showroom class for handling sales and rentals
class Showroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Showroom")
        
        self.sales = []
        self.rentals = []
        
        self.create_widgets()

    def create_widgets(self):
        # Section for adding cars for sale
        tk.Label(self.root, text="Add Car for Sale").grid(row=0, column=0, columnspan=2)
        tk.Label(self.root, text="Make:").grid(row=1, column=0)
        self.make_sale = tk.Entry(self.root)
        self.make_sale.grid(row=1, column=1)

        tk.Label(self.root, text="Model:").grid(row=2, column=0)
        self.model_sale = tk.Entry(self.root)
        self.model_sale.grid(row=2, column=1)

        tk.Label(self.root, text="Year:").grid(row=3, column=0)
        self.year_sale = tk.Entry(self.root)
        self.year_sale.grid(row=3, column=1)

        tk.Label(self.root, text="Price:").grid(row=4, column=0)
        self.price_sale = tk.Entry(self.root)
        self.price_sale.grid(row=4, column=1)

        tk.Button(self.root, text="Add Sale", command=self.add_sale).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Calculate Sales", command=self.calculate_sales).grid(row=6, column=0, columnspan=2)

        # Section for adding cars for rent
        tk.Label(self.root, text="Add Car for Rent").grid(row=0, column=2, columnspan=2)
        tk.Label(self.root, text="Make:").grid(row=1, column=2)
        self.make_rent = tk.Entry(self.root)
        self.make_rent.grid(row=1, column=3)

        tk.Label(self.root, text="Model:").grid(row=2, column=2)
        self.model_rent = tk.Entry(self.root)
        self.model_rent.grid(row=2, column=3)

        tk.Label(self.root, text="Year:").grid(row=3, column=2)
        self.year_rent = tk.Entry(self.root)
        self.year_rent.grid(row=3, column=3)

        tk.Label(self.root, text="Rent Price:").grid(row=4, column=2)
        self.price_rent = tk.Entry(self.root)
        self.price_rent.grid(row=4, column=3)

        tk.Button(self.root, text="Add Rent", command=self.add_rent).grid(row=5, column=2, columnspan=2)
        tk.Button(self.root, text="Calculate Rentals", command=self.calculate_rentals).grid(row=6, column=2, columnspan=2)

        # Listbox for displaying sales and rentals
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=7, column=0, columnspan=4)

    def add_sale(self):
        car = Car(self.make_sale.get(), self.model_sale.get(), self.year_sale.get(), float(self.price_sale.get()))
        self.sales.append(car)
        self.listbox.insert(tk.END, f"Sale: {car}")
        self.clear_entries(self.make_sale, self.model_sale, self.year_sale, self.price_sale)

    def add_rent(self):
        car = Car(self.make_rent.get(), self.model_rent.get(), self.year_rent.get(), float(self.price_rent.get()))
        self.rentals.append(car)
        self.listbox.insert(tk.END, f"Rent: {car}")
        self.clear_entries(self.make_rent, self.model_rent, self.year_rent, self.price_rent)

    def calculate_sales(self):
        total_sales = sum(car.price for car in self.sales)
        self.listbox.insert(tk.END, f"Total Sales: ${total_sales}")

    def calculate_rentals(self):
        total_rentals = sum(car.price for car in self.rentals)
        self.listbox.insert(tk.END, f"Total Rentals: ${total_rentals}")

    def clear_entries(self, *entries):
        for entry in entries:
            entry.delete(0, tk.END)

# Main application
root = tk.Tk()
app = Showroom(root)
root.mainloop()







import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.master, text='C', padx=20, pady=20, font=('Arial', 18),
                  command=self.clear).grid(row=row_val, column=0, columnspan=4)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
    



