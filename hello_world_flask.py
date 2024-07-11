# GitHub Repository: https://github.com/sascott9655/cst205_hello_world_flask

# hello_flask.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)


# route decorator binds a function to a URL
@app.route('/')
def favoriteAcronyms():
  return '<p>Me : ASCII, because it is very important to computer science</p> <p> Myself : LOL, because it is popular in our modern culture</p> <p> I : ILY, because it is important to say I love you</p>'

@app.route('/sam')
def myfavoriteAcronym():
  return render_template('templates.html')