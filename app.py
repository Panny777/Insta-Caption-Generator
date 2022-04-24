import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        caption = request.form["caption"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_prompt(caption),
            temperature=0.6,
            max_tokens=100
        )

        hashtags = openai.Completion.create(
            engine="text-davinci-002",
            prompt=generate_hashtags(caption),
            temperature=0.6,
            max_tokens=100
        )

        return redirect(url_for("index", result=response.choices[0].text + "\n" +hashtags.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(caption):
    return """compose an instagram caption about
""" + caption

def generate_hashtags(caption):
    return """generate three instagram hashtag about""" + caption

