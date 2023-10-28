import  random
from flask import Flask, redirect, render_template, url_for, flash, request
from Topics import get_it_concepts_with_subtopics
from OpenAI import open_ai_response
from Prompt import prompt

app= Flask(__name__)
topic=random.choice(get_it_concepts_with_subtopics())
# concept=topic["concpet"]
subtopic=topic["subtopic"]

#create the prompt object, pass concept and subtopic as arguments
prompt = prompt(subtopic=subtopic)



#get the data and divide the data properly





@app.route("/")
def main():


   return  render_template("index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
