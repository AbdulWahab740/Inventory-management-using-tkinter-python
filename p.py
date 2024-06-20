from tkinter import *
from tkinter import ttk

root = Tk()

f1 = LabelFrame(root, text="Frame")
f1.pack()

my_can = Canvas(f1)
my_can.pack(side="left")

scrll = ttk.Scrollbar(f1, orient='vertical', command=my_can.yview)
scrll.pack(side=RIGHT, fill=Y)

my_can.configure(yscrollcommand=scrll.set)

# Corrected binding for the Configure event
my_can.bind("<Configure>", lambda e: my_can.configure(scrollregion=my_can.bbox("all")))

my_frame = Frame(my_can)
my_can.create_window((0, 0), window=my_frame, anchor='nw')

# Adding some widgets to the scrollable frame
for i in range(20):
    Label(my_frame, text=f"Label {i+1}").pack()

root.mainloop()
