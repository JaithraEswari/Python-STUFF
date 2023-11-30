import tkinter as tk

windows = tk.Tk()
windows.title("Mile to Km Converter")
windows.config(padx=20,pady=20)

def calculate():
    number = entry.get()
    km = int(number) * 1.6
    label3.config(text= km)

label1 = tk.Label(text="Miles")
label1.grid(column=3, row=0)

entry = tk.Entry(width=10)
entry.grid(column=2,row=0)

label2 = tk.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tk.Label(text="0")
label3.grid(column=2, row=1)

label4 = tk.Label(text="Km")
label4.grid(column=3, row=1)

button = tk.Button(text="Click Me", command=calculate)
button.grid(column=2, row=3)



windows.mainloop()
