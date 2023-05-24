import tkinter as tk
from tkinter import messagebox
from functools import partial
 
 # Declaration of global variable
temp_value = "Celsius"

# Stores the temperature's value
def store_temp(get_temp):
    global temp_value
    temp_value = store_temp

# Temperature conversion
def convert(label, input):
   temp = input.get()

   # Convert from celsius to fahrenheit
   if temp_value == 'Celsius':    
        f = float((float(temp) * 9 / 5 ) + 32)
        label.config(text = "%.1f Fahrenheit" % f)
        messagebox.showinfo("Temperature Converter",
                        "Successfully converted to Fahrenheit ", )
        
        # Convert from fahrenheit to celsius
        if temp_value == 'Fahrenheit':
            c = float((float(temp) * 9 / 5 ) + 32)
            label.config(text ="%.1f Celsius" % c)
            messagebox.showinfo("Temperature Converter",
                            "Successfully converted to Celsius ", )
            return

# Create window
root = tk.Tk()
 
root.geometry('300x150 + 600 + 200')
 
root.title('Temperature Converter')
 
# Lay out widgets
root.grid_columnconfigure(1, weight = 1)
root.grid_rowconfigure(1, weight = 1)
 
inputNumber = tk.StringVar()
var = tk.StringVar()
 
# Label and entry field
input_label = tk.Label(root, text ="Enter temperature")
input_entry = tk.Entry(root, textvariable = inputNumber)
input_label.grid(row = 1)
input_entry.grid(row = 1, column = 1)
result_label = tk.Label(root)
result_label.grid(row = 3, columnspan = 4)
 
# Drop down setup
dropDownList = ["Celsius", "Fahrenheit"]
drop_down = tk.OptionMenu(root, var, *dropDownList,
                          command = store_temp)
var.set(dropDownList[0])
drop_down.grid(row = 1, column = 2)
 
# Button widget
call_convert = partial(convert, result_label,
                       inputNumber)
result_button = tk.Button(root, text ="Convert",
                          command = call_convert)
result_button.grid(row = 2, columnspan = 2)
 
# Infitinte loop
root.mainloop()
