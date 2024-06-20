import tkinter as tk
from datetime import date
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("1280x700")
        self.bg_color = "#074463"
        self.title = tk.Label(self.root, text="Morgan's Inventory Management System", font=("Montserrat", 15, "bold"),
                            relief="raised", bd=5, bg=self.bg_color, fg='white', pady=5)
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Customer Information
        F1 = tk.LabelFrame(self.root, text="Customer Information", font=("Montserrat", 11, "bold"),
                        bg=self.bg_color, fg='gold')
        F1.grid(row=1, column=0, sticky="ew")

        self.name_label = tk.Label(F1, text="Client Name:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                fg='white', pady=3)
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(F1, width=30, font="Montserrat 11")
        self.name_entry.grid(row=0, column=1, padx=10)

        self.date_label = tk.Label(F1, text="Date:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                fg='white', pady=5)
        self.date_label.grid(row=0, column=2)
        self.date_entry = tk.Entry(F1, width=15, font="Montserrat 11")
        self.date_entry.grid(row=0, column=3, padx=10)
        today = date.today()
        self.default_date = today.strftime("       %Y-%m-%d    ")  # Format as YYYY-MM-DD
        self.date_entry.insert(0, self.default_date)
        self.slip_number =0
        self.slip_label = tk.Label(F1, text=f"Slip# {self.slip_number}", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                fg='white', pady=5)
        self.slip_label.grid(row=0, column=4)
        self.new_slip_button = tk.Button(F1, text="New Slip", font=("Montserrat", 9, "bold"), 
                                        width=9, height=2, relief='raised', bd=4, bg='white', fg=self.bg_color) #command=self.load_slip_number,
        self.new_slip_button.grid(row=0, column=5, padx=10)

        # Add Item
        F2 = tk.LabelFrame(self.root, text="ADD ITEMS", font=("Montserrat", 11, "bold"),
                        bg=self.bg_color, fg='gold')
        F2.grid(row=2, column=0, sticky="ew")

        self.item_label = tk.Label(F2, text="Item:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                fg='white', pady=3)
        self.item_label.grid(row=0, column=0)
        self.item_entry = tk.Entry(F2, width=15, font="Montserrat 11")
        self.item_entry.grid(row=0, column=1, padx=10)

        self.quantity_label = tk.Label(F2, text="Quantity:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                    fg='white', pady=3)
        self.quantity_label.grid(row=0, column=2)
        self.quantity_entry = tk.Entry(F2, width=15, font="Montserrat 11")
        self.quantity_entry.grid(row=0, column=3, padx=10)

        self.buying_label = tk.Label(F2, text="Buying Price:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                    fg='white', pady=3)
        self.buying_label.grid(row=0, column=4)
        self.buying_entry = tk.Entry(F2, width=15, font="Montserrat 11")
        self.buying_entry.grid(row=0, column=5, padx=10)

        self.selling_label = tk.Label(F2, text="Selling Price:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
                                    fg='white', pady=3)
        self.selling_label.grid(row=0, column=6)
        self.selling_entry = tk.Entry(F2, width=15, font="Montserrat 11")
        self.selling_entry.grid(row=0, column=7, padx=10)

        
    def create_circle_button(self, parent, radius, color, command):
        canvas = tk.Canvas(parent, width=radius*2, height=radius*2, bg=color, highlightthickness=0)
        canvas.grid(row=0, column=0, pady=5)

        # Create circular shape
        canvas.create_oval(0, 0, radius*2, radius*2, fill=color, outline="")

        # Create X symbol inside the circle
        x_size = 7  # Adjust the size of the X symbol
        x_pos = radius - x_size // 2
        canvas.create_line(x_pos, x_pos, x_pos + x_size, x_pos + x_size, width=2, fill="white")
        canvas.create_line(x_pos + x_size, x_pos, x_pos, x_pos + x_size, width=2, fill="white")

        # Bind click event to the button
        canvas.bind("<Button-1>", lambda event: command())

    def load_items(self):
        try:
            self.invent_item = tk.Label(self.inventory_frame, text="Items Inventory", font=("Montserrat", 13, "bold "),
                                        bg=self.bg_color, fg='gold')
            self.invent_item.grid(row=0, column=0)

            myscrollbar = tk.Scrollbar(self.inventory_frame, orient="vertical")
            myscrollbar.grid(row=0, column=1, sticky="ns")

            # Configure scrollbar for inventory_frame
            self.inventory_frame.grid_rowconfigure(0, weight=1)  # Make the first row of inventory_frame expandable
            self.inventory_frame.grid_columnconfigure(0, weight=1)  # Make the first column of inventory_frame expandable

            with open("inventory.txt", "r") as file:
                for idx, line in enumerate(file):
                    try:
                        item, quantity, price, retail = line.strip().split(",")
                        self.add_item_to_gui(item, quantity, price, retail, row=idx+1)  # Start from row 1
                    except ValueError:
                        print(f"Ignore line in inventory file: {line.strip()}")
        except FileNotFoundError:
            pass
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()