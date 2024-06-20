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
        self.title = tk.Label(root, text="Morgan's Inventory Management System", font=("Montserrat", 15, "bold"),
                              relief="raised", bd=5, bg=self.bg_color, fg='white', pady=5)
        self.title.pack(fill="x")

        # Customer Information
        F1 = tk.LabelFrame(self.root, text="Customer Information", font=("Montserrat", 11, "bold"),
                           bg=self.bg_color, fg='gold',height=0)
        F1.pack(anchor='w',fill="x")

        self.name_label = tk.Label(F1, text="    Client Name:", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=3)
        self.name_label.pack(side="left")
        self.name_entry = tk.Entry(F1,width=30,font="Montserrat 11")
        self.name_entry.pack(side="left",pady=20,padx=15)

        self.date_label = tk.Label(F1, text="                 Date:", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=5,)
        self.date_label.pack(side="left")
        self.date_entry = tk.Entry(F1,width=15,font="Montserrat 11")
        self.date_entry.pack(side="left",pady=20,padx=15)
        self.slip_number = 0
        self.slip_label = tk.Label(F1, text=f"       Slip#  {self.slip_number}               ", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=5)
        self.slip_label.pack(side="left")
        self.new_slip_button = tk.Button(F1, text="  New Slip    ",font=("Montserrat", 9, "bold"), command=self.load_slip_number,width=9,height=2,relief='raised',bd=4,bg='white',fg=self.bg_color)
        self.new_slip_button.pack(padx=15, pady=20,side='left')

        self.remove_slip_button = tk.Button(F1, text="  Clear Slip  ",font=("Montserrat", 9, "bold"), command=self.remove_slip_number,width=9,height=2,relief='raised',bd=4,bg='white',fg=self.bg_color)
        self.remove_slip_button.pack(padx=25, pady=20,side='left')

        today = date.today()
        self.default_date = today.strftime("       %Y-%m-%d    ")  # Format as YYYY-MM-DD
        self.date_entry.insert(0, self.default_date)

        # Add Item
        F2 = tk.LabelFrame(self.root, text="ADD ITEMS", font=("Montserrat", 11, "bold"),
                           bg=self.bg_color, fg='gold',height=0)
        F2.pack(anchor='w',fill="x")

        self.item_label = tk.Label(F2, text="   Item:", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=3)
        self.item_label.pack(side="left")
        self.item_entry = tk.Entry(F2,width=15,font="Montserrat 11")
        self.item_entry.pack(side="left",pady=20,padx=15)
        self.quantity_label = tk.Label(F2, text="Quantity:", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=3)
        self.quantity_label.pack(side="left")
        self.quantity_entry = tk.Entry(F2,width=15,font="Montserrat 11")
        self.quantity_entry.pack(side="left",pady=20,padx=15)
        self.buying_label = tk.Label(F2, text="Buying Price:", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=3)
        self.buying_label.pack(side="left")
        self.buying_entry = tk.Entry(F2,width=15,font="Montserrat 11")
        self.buying_entry.pack(side="left",pady=20,padx=15)

        self.selling_label = tk.Label(F2, text="Selling Price:  ", font=("Montserrat", 15, "bold"), bg=self.bg_color, fg='white',pady=3)
        self.selling_label.pack(side="left")
        self.selling_entry = tk.Entry(F2,width=15,font="Montserrat 11")
        self.selling_entry.pack(side="left",pady=20,padx=15)

        self.add_button = tk.Button(F2, text="Add Item", command=self.add_item,font=("Montserrat", 9, "bold"),width=9,height=2,relief='raised',bd=4,bg='white',fg=self.bg_color)
        self.add_button.pack(padx=15, pady=20,side='left')

        self.inventory_frame = tk.Frame(self.root,
                                     bg=self.bg_color, width=500)
        
        self.inventory_frame.pack(side='left',fill='both')  # Pack on the left side, fill available space
        
        # Add widgets to the inventory frame

        self.bill_frame = tk.LabelFrame(self.root, text="Bill Area", font=("Montserrat", 11, "bold"),
                                        bg=self.bg_color, fg='gold', height=45)
        self.bill_frame.pack(anchor='w',fill='both')  # Pack on the left side, fill available space
        # self.bill_frame.config(
        self.bill_label = tk.Label(self.bill_frame, text="                               Bill Area                                 ", font=("Montserrat", 16, "bold "),bg=self.bg_color, fg='white',pady=3)
        self.bill_label.pack()

        scrol_y = tk.Scrollbar(self.bill_frame,orient="vertical")
        self.txtarea = tk.Text(self.bill_frame,yscrollcommand=scrol_y.set,bg=self.bg_color,font=("Times New Roman",11),fg='white',height=15)
        scrol_y.pack(side=tk.RIGHT,fill='y')
        scrol_y.config(command=self.txtarea.yview)

        self.txtarea.pack_configure()
        self.txtarea.insert(tk.END,"\n\t\t\t Welcome to AW Inventory Management")
        self.txtarea.insert(tk.END,f"\n\n Customer Name: {self.name_entry.get()}")
        self.txtarea.insert(tk.END,f"\n Date: {self.date_entry.get()}")
        self.txtarea.insert(tk.END,f"\n Slip # {self.load_slip_number()}")
        self.txtarea.insert(tk.END,"\n=========================================================")
        self.txtarea.insert(tk.END,"\n  Product\t\t  Quantity \t\t   Buy Price \t\t    Sell Price ")
        self.txtarea.insert(tk.END,"\n=========================================================")
        self.load_items()

        # self.total_frame = tk.LabelFrame(self.root, text="Total Price", font=("Montserrat", 11, "bold"),
        #                                 bg=self.bg_color, fg='gold', height=45)
        # self.total_frame.pack(anchor='w',side='bottom')  
        # self.total_frame.config(width=0,)
        self.add_button = tk.Button(self.bill_frame, text="Total Price", command=self.totalBuyPrice,font=("Montserrat", 9, "bold"),width=9,height=2,relief='raised',bd=4,bg='white',fg=self.bg_color)
        self.add_button.pack(side='left')
        # self.total_label = tk.Label(self.bill_frame, text=" Bill Area ", font=("Montserrat", 16, "bold "),bg=self.bg_color, fg='white',pady=3)
        # self.total_label.pack()
        
        self.priceVar = tk.DoubleVar()
        self.retailVar = tk.DoubleVar()
        self.total_buy_price = 0
        self.total_sell_price = 0


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
                              relief="raised", bg=self.bg_color, fg='white').pack()
            tsp = self.total_sell_price
            tk.Label(self.bill_frame,text=f"Total Selling Price: {tsp}",font=("Montserrat", 9, "bold"),
                              relief="raised", bg=self.bg_color, fg='white').pack()
            
    def add_item_to_gui(self, item, quantity, price, retail):
        self.item_var = tk.IntVar()
        # my_can = tk.Canvas(self.inventory_frame)
        # my_can.pack(side="left")

        # scrll = ttk.Scrollbar(self.inventory_frame, orient='vertical', command=my_can.yview)
        # scrll.pack(side='right', fill='y')


        item_frame = tk.Frame(self.inventory_frame)  # Use self.my_can instead of self.inventory_frame
        item_frame.pack(fill=tk.X)  # Ensure new items start on a new line

        # Define a command function to set the current item
        def set_current_item_command():
            self.current_item = item
            print(f"Current item set to: {self.current_item}")  # Debug print

        # Create and pack widgets in the item frame
        tk.Label(item_frame, text=f"", font="Montserrat 11 ").pack(side=tk.LEFT, padx=5, pady=2)
        self.create_circle_button(item_frame, 10, "red", command=lambda: self.remove_item(item))
        check_button = tk.Checkbutton(item_frame, text=f"   {item} ({quantity})", font="Montserrat 10 ",
                                    variable=self.item_var, command=set_current_item_command)
        check_button.pack(side=tk.LEFT, padx=5, pady=2)

        self.quantityVar = tk.IntVar()

        # Add price button and label
        price_label = tk.Label(item_frame, text=f" Buy: Rs({price})", font="Montserrat 10 ")
        price_label.pack(side=tk.LEFT, padx=5, pady=2)
        retial_label = tk.Label(item_frame, text=f" Sell: Rs({retail})", font="Montserrat 10 ")
        retial_label.pack(side=tk.LEFT, padx=5, pady=2)

        # Add quantity Spinbox and order button
        spinbox = tk.Spinbox(item_frame, from_=0, to=100, textvariable=self.quantityVar)
        spinbox.pack(side=tk.LEFT, padx=5, pady=2)
        spinbox.bind("<FocusOut>", lambda event, item=item, spinbox=spinbox: self.update_quantity(event, item, spinbox.get()))

        order_button = tk.Button(item_frame, text="Place Order", command=self.order_item)
        order_button.pack(side=tk.LEFT, padx=5, pady=2)

        # # Update the canvas scroll region to include the new item frame
        # my_can.update_idletasks()        
        # my_can.configure(yscrollcommand=scrll.set)

        # # Corrected binding for the Configure event
        # my_can.bind("<Configure>", lambda e: my_can.configure(scrollregion=my_can.bbox("all")))
        # # Create a button for placing order

    def create_circle_button(self,parent, radius, color, command):
        canvas = tk.Canvas(parent, width=radius*2, height=radius*2, bg=color, highlightthickness=0)
        canvas.pack(side='left',pady=5)

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
                                        bg=self.bg_color, fg='gold', )
            self.invent_item.pack()
            myscrollbar=tk.Scrollbar(self.inventory_frame,orient="vertical")
            myscrollbar.pack(side="right",fill="y")
            with open("inventory.txt", "r") as file:
                for line in file:
                    try:
                        item, quantity, price, retail = line.strip().split(",")
                        self.add_item_to_gui(item, quantity, price,retail)
                    except ValueError:
                        print(f"Ignore line in inventory file: {line.strip()}")
        except FileNotFoundError:
            pass

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
