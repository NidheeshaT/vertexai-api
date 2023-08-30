from flask import Flask,request,make_response, jsonify
import google.generativeai as palm
from googletrans import Translator
import dotenv
from flask_cors import CORS
import json,os
from pydub import AudioSegment
dotenv.load_dotenv()
import subprocess

if os.environ.get("PALM_KEY",False):
    palm.configure(api_key=os.environ.get("PALM_KEY"))
else:
    print("No palm key found")
    exit(1)

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = False if os.environ.get("PRODUCTION","False")=="True" else True

support_context="Imagine you are an AI-powered personal healthcare advisor with the name Aido and mental health support chatbot. A user has just reached out to you seeking guidance and support. Write a response that empathetically addresses their concerns, provides accurate healthcare information, and offers practical advice to improve their overall well-being. Keep in mind the importance of being understanding, non-judgmental, and respectful throughout the conversation."

def palmCall(message:str,context:str,history:list):
    valid_history=[]
    for i,h in enumerate(history):
        if "content" in h and "author" in h:
            valid_history.append(h)
    valid_history.append({"content":message,"author":"user"})
    reply=palm.chat(context=context,messages=valid_history)
    return reply.last

@app.post("/query")
def query():
    try:
        req_data=request.json #message,context,history:list of chat messages
        message=req_data.get("message","")
        context=req_data.get("context","")
        history=req_data.get("history",[])
        response=palmCall(message,context,history)
        return f"{response}"
    except Exception as e:
        return makexresponse("Server error",500)

@app.post("/support")
def support():
    try:
        req_data=request.json #message,context,history:list of chat messages
        message=req_data.get("message")
        context=req_data.get("context","")
        history=req_data.get("history",[])
        response=palmCall(message,support_context+context,history)
        return f"{response}"
    except Exception as e:
        return make_response("Server error",500)

@app.post("/convertToSpeech")
def convertToSpeech():
    try:
        audio_file = request.files['audio']
        audio_file.save("./audio.mp3")
        sound = AudioSegment.from_mp3("./audio.mp3")
        sound.export("./output.ogg", format="ogg")
        result = subprocess.run(["rhubarb","-f","json","./output.ogg"] , capture_output=True)
        return f"{result.stdout.decode('utf-8')}"
    except Exception as e:
        print(e)
        return make_response(f"{e}",500)

@app.post("/translate")
def translate1():
    try:
        translator=Translator()
        req_data=request.json
        message=req_data.get("message","")
        language=req_data.get("language","en-IN")

        response=translator.translate(message,dest=language).text
        return response
    except Exception as e:
        print(e)
        return make_response(f"{e}",500)
    
if __name__=='__main__':
   app.run(debug=True, port=8001)
