from tkinter import *
import numpy as np
from app import ChatBot

class GUI:
    def __init__(self, master, ai):
        self.master = master
        master.title(ai.name)
        master.geometry("400x600")
        self.ai = ai
        self.user_input = ""

        self.layout()
    
    def layout(self):
        l1 = Label(self.master, text=self.ai.name)
        l1.config(font=("Courier", 18))
        l1.pack()

        self.text_box = Text(self.master, height=30, width=40)
        self.text_box.pack(fill="both", expand=True)

        self.entry_line = Entry(self.master)
        self.entry_line.pack(fill="x")

        self.entry_line.insert(0, np.random.choice(["Chat with me...", "Dispatch me...", "Converse with me..."]))
        self.entry_line.bind("<FocusIn>", self.entry_line.delete(0, "end"))
        self.entry_line.bind("<Return>", self.output_res)

    def output_res(self):
        self.user_input = self.entry_line.get()

        if self.ai.wake_up == True:
            r = self.ai.generate_response(self.user_input)
            self.text_box.insert(END, r + '\n')
        else:
            r = self.ai.welcome_prompt()
            self.text_box.insert(END, r + '\n')

root = Tk()
GUI(root, ChatBot(name="Dev"))
root.mainloop()