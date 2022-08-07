import transformers
from gtts import gTTS
import numpy as np
import os
from tkinter import ttk
from tkinter import *

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.wake_up = False
        self.nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")

    def welcome_prompt(self, init_msg):
        self.wake_up = True
        if self.name.lower() in init_msg.lower():
            res = np.random.choice([f"Hello I am {self.name} the AI, what can I do for you?", f"Hello, my name is {self.name} the AI. What can I help you with?"])
            return res
        else:
            res = self.generate_response(init_msg)
            return res

    def generate_response(self, feed):
        if any(i in feed.lower() for i in ["what's your name", "what is your name"]):
            res = np.random.choice([f"I'm {self.name}.", f"My name is {self.name}."])        
        else:
            chatter = self.nlp(transformers.Conversation(feed), pad_token_id=50256)
            res = str(chatter)
            res = res[res.find("bot >> ")+6:].strip()
        return res
    
    def text_to_speech(self, text):
        tts_en = gTTS(text=text, lang="en", slow=False)
        filename = "res"
        tts_en.save(filename+".mp3")
        os.system(f"start {filename}.mp3")

    def clear_console(self):
        os.system('powershell "clear"')

if __name__ == '__main__':
    ai = ChatBot(name="Dev")
    ai.clear_console()

    while True:
        if ai.wake_up == True:
            user_res = input("user >> ")
            r = ai.generate_response(user_res)
            print(r)

        else:
            user_res = input("user >> ")
            r = ai.welcome_prompt(user_res)
            print(r)