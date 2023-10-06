import os
import openai
import dotenv
def open_ai_response():
  config = dotenv.dotenv_values(".env")
  openai.api_key = config['OPENAI_API_KEY']


  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": ""


      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response