import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

file_history = r'C:\Users\460226\Desktop\coding\bot+ai\learn_ai\chat_history.json' #change ur own path

load_dotenv()

api = os.getenv('api')

genai.configure(api_key=api)

model = genai.GenerativeModel('gemini-2.0-flash')

generation_config = {
"temperature": 0.7,
"max_output_tokens": 256,
"top_p": 1
}

try:
    with open(file_history,'r',encoding='utf-8') as f:
        history = json.load(f)
except (FileNotFoundError,json.JSONDecodeError):
    print('sonething error')
    history = []


while True:
    prompt = input('input: ')
    if prompt == '/reset':
        print('chat is reseted')
        history=[]
    else:
        history.append({"role": "user", "parts":prompt})
        respond = model.generate_content(
            history,
            generation_config=generation_config
        )
        print('\nGemini: ',respond.text)
        history.append({"role": "model", "parts":respond.text})
        with open(file_history,'w',encoding='utf-8') as f:
            json.dump(history,f,indent=3,ensure_ascii=False)
    
