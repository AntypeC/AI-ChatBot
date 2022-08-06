import transformers
from gtts import gTTS
import os
import numpy as np


class ChatBot:
    def __init__(self, name):
        self.name = name
        self.wake_up = False
        self.nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")

    def welcome_prompt(self):
        self.wake_up = True
        res = np.random.choice([f"Hello, I'm {self.name}, how can I help you?", f"Hello there, I'm {self.name} the AI, how may I assist you?", f"Sup, my name is {self.name}, how can I help you?"])
        return res

    def generate_response(self, feed):
        chat = self.nlp(transformers.Conversation(feed), pad_token_id=50256)
        res = str(chat)
        res = res[res.find("bot >> ")+6:].strip()
        return res
    
    def text_to_speech(self, input_res):
        tts_en = gTTS(text=input_res, lang="en", slow=False)
        filename = "res"
        tts_en.save(filename+".mp3")
        os.system(f"start {filename}.mp3")

    def clear_console(self):
        os.system('powershell "clear"')

if __name__ == '__main__':
    ai = ChatBot(name="Dev")
    ai.clear_console()
    input("user >> ")

    while True:
        if ai.wake_up == True:
            if any(i in user_res.lower() for i in ["what's your name", "what is your name"]):
                r = np.random.choice([f"I'm {ai.name}.", f"My name is {ai.name}."])        
            else:
                r = ai.generate_response(user_res)
            
            print(r)
            ai.text_to_speech(r)
            user_res = input("user >> ")

        else:
            r = ai.welcome_prompt()
            print(r)
            ai.text_to_speech(r)
            user_res = input("user >> ")