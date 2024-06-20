import tkinter as tk
from datetime import date
from tkinter.messagebox import showinfo,showwarning,askyesno
from tkinter import ttk
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("1280x700")
        self.bg_color = "#074463"
        self.item_grid_row = 2
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
        self.add_button = tk.Button(F2, text="Add Item", command=self.add_item, font=("Montserrat", 9, "bold"),
                            width=9, height=2, relief='raised', bd=4, bg='white', fg=self.bg_color)
        self.add_button.grid(row=0, column=8, padx=15, pady=20)

        self.inventory_frame = tk.Frame(self.root, bg=self.bg_color, width=500)
        self.inventory_frame.grid(row=3, column=0, sticky="nsew")  # Grid with sticky to fill available space
        # self.inv_label = tk.Label(self.inventory_frame, text="Buying Price:", font=("Montserrat", 15, "bold"), bg=self.bg_color,
        #                             fg='white', pady=3)
        # self.inv_label.grid(row=0, column=0)
        myscrollbar = tk.Scrollbar(self.inventory_frame, orient="vertical")
        myscrollbar.grid(row=0, column=1, sticky="ns")

        self.my_can = tk.Canvas(self.inventory_frame, yscrollcommand=myscrollbar.set)
        self.my_can.grid(row=0, column=0, sticky="nsew")

        myscrollbar.config(command=self.my_can.yview)

        # Create a frame inside the canvas for the items
        self.item_frame = tk.Frame(self.my_can)
        self.my_can.create_window((0, 0), window=self.item_frame, anchor='nw')

        self.my_can.bind("<Configure>", lambda e: self.my_can.configure(scrollregion=self.my_can.bbox("all")))
        self.load_items()
        self.bill_frame = tk.LabelFrame(self.root, text="Bill Area", font=("Montserrat", 11, "bold"),
                                        bg=self.bg_color, fg='gold', height=45)
        self.bill_frame.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)  # Grid with sticky to fill available space
        self.bill_label = tk.Label(self.bill_frame, text="Bill Area", font=("Montserrat", 16, "bold "),
                                bg=self.bg_color, fg='white', pady=3)
        self.bill_label.grid(row=0, column=0, columnspan=2)  # Span across two columns

        scrol_y = tk.Scrollbar(self.bill_frame, orient="vertical")
        scrol_y.grid(row=1, column=1, sticky="ns")  # Grid scrollbar to the right, sticky to fill vertically

        self.txtarea = tk.Text(self.bill_frame, yscrollcommand=scrol_y.set, bg=self.bg_color,
                            font=("Times New Roman", 11), fg='white', height=15)
        self.txtarea.grid(row=1, column=0, sticky="nsew")  # Grid text area to the left, sticky to fill available space

        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.insert(tk.END, "\n\t\t\t Welcome to AW Inventory Management")
        self.txtarea.insert(tk.END, f"\n\n Customer Name: {self.name_entry.get()}")
        self.txtarea.insert(tk.END, f"\n Date: {self.date_entry.get()}")
        self.txtarea.insert(tk.END, f"\n Slip # {self.load_slip_number()}")
        self.txtarea.insert(tk.END, "\n=========================================================")
        self.txtarea.insert(tk.END, "\n  Product\t\t  Quantity \t\t   Buy Price \t\t    Sell Price ")
        self.txtarea.insert(tk.END, "\n=========================================================")

        self.add_button_total = tk.Button(self.bill_frame, text="Total Price", command=self.totalBuyPrice,
                                        font=("Montserrat", 9, "bold"), width=9, height=2, relief='raised', bd=4,
                                        bg='white', fg=self.bg_color)
        self.add_button_total.grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.priceVar = tk.DoubleVar()
        self.retailVar = tk.DoubleVar()
        self.total_buy_price = 0
        self.total_sell_price = 0

    def create_circle_button(self, parent, radius, color, command):
        canvas = tk.Canvas(parent, width=radius*2, height=radius*2, bg=color, highlightthickness=0)
        
        # Create circular shape
        canvas.create_oval(0, 0, radius*2, radius*2, fill=color, outline="")
        
        # Create X symbol inside the circle
        x_size = 7  # Adjust the size of the X symbol
        x_pos = radius - x_size // 2
        canvas.create_line(x_pos, x_pos, x_pos + x_size, x_pos + x_size, width=2, fill="white")
        canvas.create_line(x_pos + x_size, x_pos, x_pos, x_pos + x_size, width=2, fill="white")
        
        # Bind click event to the button
        canvas.bind("<Button-1>", lambda event: command())
        
        return canvas  

    def load_items(self):
        try:
            self.invent_item = tk.Label(self.inventory_frame, text="Items Inventory", font=("Montserrat", 13, "bold "),
                                        bg=self.bg_color, fg='gold')
            self.invent_item.grid(row=0, column=0, pady=5, sticky="w")

            with open("inventory.txt", "r") as file:
                for idx, line in enumerate(file):
                    try:
                        item, quantity, price, retail = line.strip().split(",")
                        self.add_item_to_gui(item, quantity, price, retail)  # Add item to GUI
                    except ValueError:
                        print(f"Ignore line in inventory file: {line.strip()}")

        except FileNotFoundError:
            pass
        # self.total_label = tk.Label(self.bill_frame, text=" Bill Area ", font=("Montserrat", 16, "bold "),bg=self.bg_color, fg='white',pady=3)
        # self.total_label.pack()

    def load_slip_number(self):
        try:
            with open("slip_number.txt", "r") as file:
                self.slip_number = int(file.read())

                self.slip_number += 1
                self.slip_label.config(text=f"       Slip#  {self.slip_number}        ")
                self.save_slip_number() 
        except FileNotFoundError:
            self.slip_number = 0
        return self.slip_number

    def save_slip_number(self):
        with open("slip_number.txt", "w") as file:
            file.write(str(self.slip_number))

    def remove_slip_number(self):
        with open("slip_number.txt", "w") as file:
            file.write(str(0))   
            self.slip_number = 0
            self.slip_label.config(text=f"       Slip#  {self.slip_number}        ")     


    def totalBuyPrice(self):
            tbp = self.total_buy_price
            tk.Label(self.bill_frame,text=f"Total Buying Price: {tbp}",font=("Montserrat", 9, "bold"),
                              relief="raised", bg=self.bg_color, fg='white').grid(row=0, column=0, pady=5)
            tsp = self.total_sell_price
            tk.Label(self.bill_frame,text=f"Total Selling Price: {tsp}",font=("Montserrat", 9, "bold"),
                              relief="raised", bg=self.bg_color, fg='white').pack(row=0, column=1, pady=5)
            
        
    def add_item_to_gui(self, item, quantity, price, retail):
        
    # Create a new frame inside the canvas for each item
        item_frame = self.item_frame # Use self.my_can instead of self.inventory_frame
        self.item_var = tk.IntVar()
        # Define a command function to set the current item
        def set_current_item_command():
            self.current_item = item
            print(f"Current item set to: {self.current_item}")  # Debug print
        
        # Create and grid widgets in the item frame
        tk.Label(item_frame, text=f"", font="Montserrat 11 ").grid(row=self.item_grid_row, column=0, padx=5, pady=2)
        self.create_circle_button(item_frame, 10, "red", command=lambda: self.remove_item(item)).grid(row=self.item_grid_row, column=1, padx=5, pady=2)
        
        check_button = tk.Checkbutton(item_frame, text=f"   {item} ({quantity})", font="Montserrat 10 ",
                                    variable=self.item_var, command=set_current_item_command)
        check_button.grid(row=self.item_grid_row, column=2, padx=5, pady=2)
        
        self.quantityVar = tk.IntVar()
        
        price_label = tk.Label(item_frame, text=f" Buy: Rs({price})", font="Montserrat 10 ")
        price_label.grid(row=self.item_grid_row, column=3, padx=5, pady=2)
        
        retial_label = tk.Label(item_frame, text=f" Sell: Rs({retail})", font="Montserrat 10 ")
        retial_label.grid(row=self.item_grid_row, column=4, padx=5, pady=2)
        
        spinbox = tk.Spinbox(item_frame, from_=0, to=100, textvariable=self.quantityVar)
        spinbox.grid(row=self.item_grid_row, column=5, padx=5, pady=2)
        spinbox.bind("<FocusOut>", lambda event, item=item, spinbox=spinbox: self.update_quantity(event, item, spinbox.get()))
        
        order_button = tk.Button(item_frame, text="Place Order", command=self.order_item)
        order_button.grid(row=self.item_grid_row, column=6, columnspan=3, padx=5, pady=2)
        
        # Grid the item frame inside the canvas
        item_frame.grid(row=self.item_grid_row, column=0, sticky="ew")
        print(self.item_grid_row)
        self.item_grid_row += 1  # Increment the grid row for the next item
        
        # Update the canvas scroll region to include the new item frame
        self.my_can.update_idletasks()
        self.my_can.configure(scrollregion=self.my_can.bbox("all"))
        # # Corrected binding for the Configure event
        # my_can.bind("<Configure>", lambda e: my_can.configure(scrollregion=my_can.bbox("all")))
        # # Create a button for placing order

    
    def add_item(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()
        price = self.buying_entry.get()
        retail = self.selling_entry.get()
        if item !="" and quantity !="" and self.buying_entry.get()!="" and self.selling_entry.get() !="":
            self.add_item_to_gui(item, quantity, price, retail)
            self.save_item(item, quantity, price,retail)
            self.item_entry.delete(0, tk.END)  # Clear the entry field after adding
            self.quantity_entry.delete(0, tk.END)  # Clear the quantity field after adding
            self.buying_entry.delete(0, tk.END)
            self.selling_entry.delete(0, tk.END)  # Clear the price field after adding
        else:
            showwarning("Warning","You have to fill out all the entries for adding the items")
    def update_quantity(self, event, item, new_quantity):
        # Find the item in your data structure (e.g., self.items) based on the item name
        for item_info in self.items:
            if item_info['item'] == item:
                # Update the quantity of the item
                item_info['quantity'] = int(new_quantity)
                break

        # Update the GUI to reflect the new quantity (if needed)
        self.update_quantity_in_gui(item, int(new_quantity))

    def get_current_quantity(self, item):
        current_quantity = 0
        with open("inventory.txt", "r") as file:
            for line in file:
                line_item, line_quantity = line.strip().split(",")[0],line.strip().split(",")[1]
                if line_item == item:
                    current_quantity = int(line_quantity)
                    break  # Stop searching after finding the item
        return current_quantity
    
    def order_item(self): 
        print(self.item_var.get())
        if self.quantityVar.get() != 0 and self.item_var.get() != 0:

            item = self.current_item
            quantity_to_order = self.quantityVar.get()
            current_quantity = self.get_current_quantity(item)
            print("Current",current_quantity)

            if quantity_to_order <= current_quantity:  # Check if ordered quantity is within available stock
                remaining_quantity = current_quantity - quantity_to_order
                print('Remaining_quantity',remaining_quantity)
                # Check if the item is in the inventory file
                found_item = False
                with open("inventory.txt", "r") as file:
                    lines = file.readlines()
                with open("inventory.txt", "w") as file:
                    for line in lines:
                        line_item, line_quantity, line_price, line_retail = line.strip().split(",")
                        if line_item == item:
                            price_list = int(line_price)
                            retail_list = int(line_retail)
                            updated_quantity = int(line_quantity) - quantity_to_order
                            print("updated_quantity",updated_quantity)
                            file.write(f"{line_item},{updated_quantity},{line_price},{line_retail}\n")
                            found_item = True
                        else:
                            file.write(line)
                if found_item:
                    # Update quantity in the GUI
                    new_quantity = updated_quantity if updated_quantity > 0 else 0
                    self.update_quantity_in_gui(item, new_quantity)
                    price_quan = price_list*(quantity_to_order)
                    retail_quan = retail_list*(quantity_to_order)
                    print("Retail Quan",retail_quan)
                    self.total_buy_price += price_quan
                    self.total_sell_price += retail_quan
                    self.txtarea.insert(tk.END, f"  {  item}\t\t       {quantity_to_order}\t\t      {price_quan}\t\t        {retail_quan}")
                    self.quantityVar.set(0)  # Reset the Spinbox value after placing order
                    
                else:
                    showwarning("Warning", f"{item} not found in inventory.")
            else:
                showwarning("Warning", f"We don't have such quantity. We only have {current_quantity} qunatity")
        else:
            showwarning("Warning", "Please select an item.")

    def update_quantity_in_gui(self, item, new_quantity):
        for child in self.inventory_frame.winfo_children():
            if isinstance(child, tk.Frame):
                for check_button in child.winfo_children():
                    if isinstance(check_button, tk.Checkbutton) and check_button.cget('text').startswith(item):
                        check_button.config(text=f"{item} ({new_quantity})")
                        return
              
    def remove_item(self, item):
        confirmed = askyesno("Confirmation", "Are you sure you want to remove this item?")
        if confirmed:
            with open("inventory.txt", "r") as file:
                lines = file.readlines()
            with open("inventory.txt", "w") as file:
                for line in lines:
                    line_item = line.strip().split(",")[0]  # Get the item name from each line
                    if line_item != item:
                        file.write(line)
            self.reload_items()                
    def reload_items(self):
        for widget in self.inventory_frame.winfo_children():
            print(widget)
            widget.destroy()
        self.load_items()
    def save_item(self, item, quantity, price, retail):
        with open("inventory.txt", "a") as file:
            file.write(f"{item},{quantity},{price},{retail}\n")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
