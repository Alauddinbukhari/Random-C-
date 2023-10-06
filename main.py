
from flask import Flask, redirect, render_template, url_for, flash, request
from Topics import get_it_concepts_with_subtopics
from OpenAI import open_ai_response
app= Flask(__name__)
topics=get_it_concepts_with_subtopics()

#get the data




@app.route("/")
def main():


   return  render_template("index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)