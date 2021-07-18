from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    calculation = miles * 1.609
    km_output.config(text=calculation)


window =Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_unit = Label(text="Miles")
miles_unit.grid(column=2, row=0)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
km_output = Label(text="0")
km_output.grid(column=1, row=1)
km_unit = Label(text="Km")
km_unit.grid(column=2, row=1)
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()