from tkinter import *
from googletrans import LANGUAGES
from tkinter import ttk
from googletrans import Translator
root = Tk()
root.geometry("500x500")
root.configure(bg = "teal")
root.title("Project 181")
list1 = list(LANGUAGES.values())

dropdown = ttk.Combobox(root, state = "readonly", values = list1)
dropdown.place(relx = 0.7, rely = 0.2, anchor = CENTER)
dropdown.set("english")
output = Label(root, text = "Output", bg = "teal", font = ("Bahnscrift Light", 15, "bold"))
output.place(relx = 0.3, rely = 0.6, anchor = CENTER)
dropdown2 = ttk.Combobox(root, state = "readonly", value = list1, width = 3)
dropdown2.place(relx = 0.7, rely = 0.6, anchor = CENTER)
dropdown2.set("Choose output language")
text = Text(root, bg = "teal", font = ("Bhanschrift Light", 15), wrap = WORD, height = 20, width = 10, padx = 15, pady = 15)
text.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn1 = Button(root, text = "Translate", font = ("Helvetica", 15), bg = "white", activebackground = "teal", fg = "Black", relief = FLAT, pady = 10)
btn1.lace(relx = 0.5, rely = 0.7, anchor = CENTER)
root.mainloop()