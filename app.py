import flask
from flask import Flask, render_template, request

# import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/recipe")
def recipe():
    return render_template('recipe.html')


@app.route("/recipes", methods=['GET'])
def recipes():

    return render_template('recipes.html')


if __name__ == '__name__':
    app.run(debug=True, port=5000)
