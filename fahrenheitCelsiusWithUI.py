from tkinter import *
window = Tk()
window.title('F/C Converter')

def count_FToC():
    data = float(entry.get())
    answer = (data-32)* 5.0/9.0
    counter.set(answer)
    temperature.set("Celsius")

def count_CToF():
    data = float(entry.get())
    answer = (data * (9/5)) + 32
    counter.set(answer)
    temperature.set("Fahrenheit")

label = Label(window,text='Fahrenheit/Celsius Converter')
label.pack()
entry = Entry(window)
entry.pack()
counter = IntVar()
counter.set(0)
temperature = StringVar()
temperature.set("")
frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
button1 = Button(frame1, text='To C', command = count_FToC)
button1.grid(row=0,column=0)
button2 = Button(frame1, text='To F', command = count_CToF)
button2.grid(row=0,column=1)
result = Label(frame2, textvariable = counter)
result.grid(row=0,column=0)
result = Label(frame2, textvariable= temperature)
result.grid(row=0,column=1)


window.mainloop()
