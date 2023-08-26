from vertexai.preview.language_models import ChatModel
import dotenv
import os
dotenv.load_dotenv()

print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

chat_model=ChatModel.from_pretrained('chat-bison@001')

chat=chat_model.start_chat()
response=chat.send_message('Hello hows the weather today?')
print(response)
