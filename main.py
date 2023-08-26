from flask import Flask,request,make_response
from vertexai.preview.language_models import ChatModel,ChatSession,ChatMessage
import dotenv
import json,os
dotenv.load_dotenv()

if not os.path.exists("./secret.json"):
    if os.environ.get("CREDENTIALS"):
        with open("secret.json","w") as f:
            f.write(os.environ.get("CREDENTIALS"))

app = Flask(__name__)
app.config["DEBUG"] = False if os.environ.get("PRODUCTION","False")=="True" else True

support_context="Imagine you are an AI-powered personal healthcare advisor with the name Aido and mental health support chatbot. A user has just reached out to you seeking guidance and support. Write a response that empathetically addresses their concerns, provides accurate healthcare information, and offers practical advice to improve their overall well-being. Keep in mind the importance of being understanding, non-judgmental, and respectful throughout the conversation."
bison_model=ChatModel.from_pretrained("chat-bison@001")

def palm(message:str,context:str,history:list):
    valid_history=[]
    for i,h in enumerate(history):
        if "content" in h and "author" in h:
            valid_history.append(ChatMessage(h["content"],h['author']))
    chat=ChatSession(model=bison_model,context=context,message_history=valid_history)
    response=chat.send_message(message)
    return response

@app.post("/query")
def query():
    try:
        req_data=request.json #message,context,history:list of chat messages
        message=req_data.get("message")
        context=req_data.get("context","")
        history=req_data.get("history",[])
        response=palm(message,context,history)
        return f"{response}"
    except Exception as e:
        return make_response("Server error",500)

@app.post("/support")
def support():
    try:
        req_data=request.json #message,context,history:list of chat messages
        message=req_data.get("message")
        context=req_data.get("context","")
        history=req_data.get("history",[])
        response=palm(message,support_context+context,history)
        return f"{response}"
    except Exception as e:
        return make_response("Server error",500)
if __name__=='__main__':
   app.run()
