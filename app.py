from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'

# Initialize the DB
db = SQLAlchemy(app)


# Create DB model for Recipes
class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Datetime, default=datetime.utcnow)

    ingredients = db.relationship('Ingredients', backref='ingredient')
    instructions = db.relationship('Instructions', backref='ingredient')

    def __repr__(self):
        return '<Name %r>' % self.id


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Datetime, default=datetime.utcnow)
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=True)

    def __repr__(self):
        return '<Name %r>' % self.id


class Instructions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.Datetime, default=datetime.utcnow)
    recipes_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=True)

    def __repr__(self):
        return '<Name %r>' % self.id


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/recipe")
def recipe():
    return render_template('recipe.html')


@app.route("/recipes")
def recipes():
    return render_template('recipes.html')


if __name__ == '__name__':
    app.run(debug=True, port=5000)
