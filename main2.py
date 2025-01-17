from tkinter  import *

from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
window = Tk()
window.title("Welcome to Wondeland")
window.geometry('600x500')
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)    


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")    



txt_edit = Text(window)
txt_edit.grid (row=0, column=1, sticky='nsew')

frame = Frame(window,relief=RIDGE,borderwidth=2)
frame.grid(row=0, column=0, sticky='ns')

btn_open = Button(frame, text="Open!",command= open_file)
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)   


btn_save = Button(frame, text="Save",command= save_file)
btn_save.grid(row=1, column=0, sticky='ew', padx=5, pady=5)   


window.mainloop()