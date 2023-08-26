from flask import Flask,request
from vertexai.preview.language_models import ChatModel,ChatSession
import dotenv
import json
dotenv.load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = True

support_context=""

@app.post("/query")
def query():
    req_data=request.json #message,context,history:list of chat messages

    chat=ChatSession(model=ChatModel.from_pretrained("chat-bison@001")) # context,history
    response=chat.send_message("Hello")#message should be applied here
    print(response)
    return f"{response}"

@app.post("/support")
def support():
    req_data=request.json #message,context,history:list of chat messages

    chat=ChatSession(model=ChatModel.from_pretrained("chat-bison@001")) # context,history
    response=chat.send_message("Hello")#message should be applied here
    print(response)
    return f"{response}"

@app.post("/tts")
def textToSpeech():
    chat=ChatSession(model=ChatModel.from_pretrained("chat-bison@001"),)
    print(chat)
    response=chat.send_message("Hello")
    print(response)
    return f"{response}"

@app.post("/stt")
def speechToText():
    chat=ChatSession(model=ChatModel.from_pretrained("chat-bison@001"),)
    print(chat)
    response=chat.send_message("Hello")
    print(response)
    return f"{response}"

if __name__=='__main__':
   app.run()
