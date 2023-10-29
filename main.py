import  random
from flask import Flask, redirect, render_template, url_for, flash, request
from Topics import get_it_concepts_with_subtopics
from OpenAI import Openai
from Prompt import prompt

app= Flask(__name__)

topic=random.choice(get_it_concepts_with_subtopics())
# concept=topic["concpet"]
sub_topic= random.choice(topic["subtopics"])
print(sub_topic)

#create the prompt object, pass concept and subtopic as arguments
prompt = prompt(subtopic=sub_topic).generate_prompt()

Open_ai=Openai(prompt)

Open_ai.gen_responce()

concept_data=Open_ai.get_response()

print(concept_data)





@app.route("/")
def main():



   return  render_template("index.html",subtopic_name=sub_topic, concept_parts= concept_data)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
