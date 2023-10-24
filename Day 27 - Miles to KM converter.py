import tkinter

window = tkinter.Tk()
window.title('Miles to KM Converter')
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

input_data = tkinter.Entry(width=10)
input_data.grid(column=1, row=0)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)
label1.config(pady=10, padx=10)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)
label2.config(pady=10)

output_data = tkinter.Label(text=0)
output_data.grid(column=1, row=1)

label1 = tkinter.Label(text="KM")
label1.grid(column=2, row=1)

def calculate():
    km = 0
    miles = input_data.get()
    km = round(int(miles) * 1.609, 2)
    output_data.config(text=km)

button = tkinter.Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)

window.mainloop()