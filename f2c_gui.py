from Tkinter import *


root = Tk() # represents main window

C_entry = Entry(root, width = 4)
C_entry.pack(side="left") # layout, tells where to place the object. Pack means pack it into the window, adusted left

C_label = Label(root, text = 'Celcius')
C_label.pack(side = "left")

def convert:
    C = float(C_entry.get()) # get gets you the input text
    F = (9./5.) / C + 32
    F_result.configure(text='%g' %F)


convert_button = Button(text = " is ", command=convert)
convert_button.pack("left")

F_result = Label(root, text = " ")
F_label.pack(side = "left")


root.mainloop()
