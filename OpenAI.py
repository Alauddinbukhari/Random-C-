import os
import openai
import dotenv

prompt = "OVERVIEW: Cryptocurrencies | HISTORY | Blockchain Technology | Use Cases | Challenges | The Future | Provide information in between 1500 and 2000 words."

def open_ai_response(prompt):
  config = dotenv.dotenv_values(".env")
  api_key = config['OPENAI_API_KEY']

  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=2000,
    api_key=api_key
  )

  response_text = response.choices[0].text
  sections = response_text.split(" | ")

  print(sections[0])  # Print the overview


open_ai_response(prompt)