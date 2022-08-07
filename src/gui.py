from tkinter import *
from xml.dom.minidom import parseString
import numpy as np
from app import ChatBot

class GUI:
    def __init__(self, master, ai):
        self.master = master
        master.title(ai.name)
        master.geometry('450x600')

        self.ai = ai
        self.user_input = ''
        # self.line_count = 0
        self.layout()
    
    def layout(self):
        l1 = Label(self.master, text=self.ai.name)
        l1.config(font=("Courier", 18))
        l1.pack()

        self.text_box = Text(self.master, height=30, width=40)
        self.text_box.config(state=DISABLED)
        self.text_box.pack(fill="both", expand=True)

        self.entry_line = Entry(self.master)
        self.entry_line.pack(fill="x")
        self.enter_func()

    def enter_func(self):
        temp_text = ["Chat with me...", "Dispatch me...", "Converse with me..."]
        self.entry_line.insert(0, np.random.choice(temp_text))
        self.entry_line.bind("<FocusIn>", self.del_temp_text)
        self.entry_line.bind("<Return>", self.output_res)

    def del_temp_text(self, *args, **kwargs):
        self.entry_line.delete(0, 'end')
        # print(*args, **kwargs)

    def output_res(self, *args, **kwargs):
        self.user_input = self.entry_line.get()
        self.entry_line.delete(0, 'end')
        self.enter_func()
        # self.line_count += 1

        if self.ai.wake_up == True:
            r = self.ai.generate_response(self.user_input)
            self.text_box['state'] = NORMAL
            # self.text_box.insert(END, f'{self.line_count}. {r}\n')
            self.text_box.insert(END, f"user >> {self.user_input}\n")
            self.text_box.insert(END, f"{self.ai.name} >> {r}\n")
            self.text_box['state'] = DISABLED
            self.ai.text_to_speech(r)
        else:
            r = self.ai.welcome_prompt(self.user_input)
            self.text_box['state'] = NORMAL
            # self.text_box.insert(END, f'{self.line_count}. {r}\n')
            self.text_box.insert(END, f"user >> {self.user_input}\n")
            self.text_box.insert(END, f"{self.ai.name} >> {r}\n")
            self.text_box['state'] = DISABLED
            self.ai.text_to_speech(r)
        # print(*args, **kwargs)

root = Tk()
GUI(root, ChatBot(name="Dev"))
root.mainloop()
