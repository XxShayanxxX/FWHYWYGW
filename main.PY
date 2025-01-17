from tkinter  import *

window = Tk()
window.title("Welcome to Wondeland")
window.geometry('600x500')
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)    

def open_file():
    pass 



txt_edit = Text(window)
frame = Frame(window,relief=RIDGE,borderwidth=2)
frame.grid(row=0, column=0, sticky='ns')

btn_open = Button(frame, text="Open!",command= open_file)
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)   


btn_save = Button(frame, text="Save",command= open_file)
btn_save.grid(row=1, column=0, sticky='ew', padx=5, pady=5)   


window.mainloop()