from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import numpy as np
import os
import pyttsx3

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.wake_up = False
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
        self.nlp = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', 160)
        self.engine.setProperty('voice', voices[0].id) #change index to change voices

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
            for _ in range(5):
                new_user_input_ids = self.tokenizer.encode(feed + self.tokenizer.eos_token, return_tensors='pt')
                bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if _ > 0 else new_user_input_ids
                chat_history_ids = self.nlp.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
                res = str(self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))

        return res
    
    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

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
