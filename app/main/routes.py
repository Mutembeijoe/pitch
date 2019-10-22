from flask import Blueprint, render_template

from app.models import Pitch

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
@main.route('/home/<string:category>')
def home(category = None):
    print(category)
    pitches = Pitch.query.all()
    return render_template('home.html', pitches = pitches)


