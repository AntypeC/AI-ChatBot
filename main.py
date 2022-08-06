import transformers
from gtts import gTTS
import os
import requests


class ChatBot:
    def __init__(self, name):
        self.name = name
        self.wake_up = False

        self.nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")

    def welcome_user(self):
        self.wake_up = True
        res = f"bot >> Hello I'm {self.name}, how can I help you?"
        res = res.replace("bot >> ", "")
        return res

    def respond(self, feed):
        chat = self.nlp(transformers.Conversation(feed), pad_token_id=50256)
        res = str(chat)
        res = res[res.find("bot >> ")+6:].strip()
        return res
    
    def speak(self, input_res):
        tts_en = gTTS(text=input_res, lang="en", slow=False)
        filename = "res"
        tts_en.save(filename+".mp3")
        os.system(f"start {filename}.mp3")

    def refresh_console(self):
        os.system('powershell "clear"')

# print(ChatBot.respond("test"))

if __name__ == '__main__':
    ai = ChatBot(name="Dev")
    input("user >> ")

    while True:
        if ai.wake_up == True:
            ai.refresh_console()
            r = ai.respond(user_res)
            print(r)
            ai.speak(r)
            user_res = input("user >> ")

        else:
            ai.refresh_console()
            r = ai.welcome_user()
            print(r)
            ai.speak(r)
            user_res = input("user >> ")
