from flask import Blueprint, render_template

from app.models import Pitch

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def home():
    pitches = Pitch.query.all()
    return render_template('home.html', pitches = pitches)


