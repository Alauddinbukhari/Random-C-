import os
import openai
import dotenv

config = dotenv.dotenv_values(".env")
API_KEY = config['OPENAI_API_KEY']
class Openai:
  def __init__(self,prompt):
    self.prompt_=prompt
    self.response=None
    self. sections_list = []


  def gen_responce(self):
    print(self.prompt_)
    self.response= openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[

      {
        "role": "user",
        "content":self.prompt_
      }
    ],
    temperature=1,
    max_tokens=2617,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
   api_key=API_KEY
     )
  def get_response(self):
    data = self.response["choices"][0]["message"]["content"]

    sections = [section.strip() for section in data.split('\n\n')]




    for section in sections:
      if section == sections[-1]:
            summary_dic = {
            "title": "Summary",
            "content": section
             }
            self.sections_list.append(summary_dic)
      else:
          try:
              section_dic = {"title": section.split("\n")[0],
                         "content": section.split("\n")[1]
                             }
              self.sections_list.append(section_dic)
          except IndexError:
              unformatted_data=section.split("\n")
              print(unformatted_data.split(":"))

    return self.sections_list






# def open_ai_response(prompt):
#
#   api_key = config['OPENAI_API_KEY']
#
#   response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#
#       {
#         "role": "user",
#         "content": prompt
#
#     ],
#     temperature=1,
#     max_tokens=2617,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0,
#     api_key=api_key
#   )
#
#   data = response["choices"][0]["message"]["content"]
#
#   sections = [section.strip() for section in data.split('\n\n')]
#
#   # Print the sections
#   sections_list = []
#
#   for section in sections:
#
#     if section == sections[-1]:
#       summary_dic = {
#         "title": "Summary",
#         "content": section
#       }
#       sections_list.append(summary_dic)
#     else:
#       section_dic = {"title": section.split("\n")[0],
#                      "content": section.split("\n")[1]}
#       sections_list.append(section_dic)
#   return sections_list
#
#
#
# open_ai_response()