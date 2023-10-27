import tkinter

window = tkinter.Tk()
window.title('Application Form')
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)

intro = tkinter.Label(text="Welcome to Application form")
intro.grid(column=0, row=0)
intro.config(pady=10)

label1 = tkinter.Label(text="Enter Full Name: ")
label1.grid(column=0, row=1)
label1.config(padx=0, pady=10)

full_name = tkinter.Entry(width=20)
full_name.grid(column=1, row=1)

label2 = tkinter.Label(text="Enter Mobile Number: ")
label2.grid(column=0, row=2)
label2.config(padx=0, pady=10)

mobile = tkinter.Entry(width=20)
mobile.grid(column=1, row=2)

label3 = tkinter.Label(text="Enter Email ID: ")
label3.grid(column=0, row=3)
label3.config(padx=0, pady=10)

email = tkinter.Entry(width=20)
email.grid(column=1, row=3)

label4 = tkinter.Label(text="Enter Password: ")
label4.grid(column=0, row=4)
label4.config(padx=0, pady=10)

password = tkinter.Entry(width=20)
password.grid(column=1, row=4)

def application():
    window1 = tkinter.Tk()
    window1.title('Application form')
    window1.minsize(width=600, height=600)
    window1.config(padx=20, pady=20)

    label5 = tkinter.Label(text="Full Name: ")
    label5.grid(column=0, row=0)
    label5.config(padx=0, pady=10)

    label6 = tkinter.Label(text="Mobile Number: ")
    label6.grid(column=0, row=1)
    label6.config(padx=0, pady=10)

    label7 = tkinter.Label(text="Email ID: ")
    label7.grid(column=0, row=2)
    label7.config(padx=0, pady=10)

    window1.mainloop()


button = tkinter.Button(text='Submit', command=application)
button.grid(column=1, row=5)


window.mainloop()
