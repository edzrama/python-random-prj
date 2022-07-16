from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Entry
input_box = Entry()
input_box.insert(END, 0)
input_box.grid(column=1, row=0)
input_box.config(width=10)

# Label
label_miles = Label(text="Miles", font=("Arial", 14))
label_miles.grid(column=2, row=0)
label_miles.config()

label_equal = Label(text="is equal to", font=("Arial", 14))
label_equal.grid(column=0, row=1)

label_value = Label(text="0", font=("Arial", 14))
label_value.grid(column=1, row=1)

label_km = Label(text="km", font=("Arial", 14))
label_km.grid(column=2, row=1)


# Button
def button_clicked():
    new_value = float(input_box.get()) * 1.609
    label_value["text"] = round(new_value, 2)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
