from flask import Blueprint, render_template,redirect
from app import db
from app.models import Pitch


main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
@main.route('/home/<string:category>')
@main.route('/home/<int:pitch_id>/<string:like>')
def home(category = None, pitch_id = None, like = None):
    if category:
        pitches = Pitch.query.filter_by(category = category)
    else:
        pitches = Pitch.query.all()

    if pitch_id and like:
        pitch = Pitch.query.get(pitch_id)
        if like == 'like':
            pitch.upvote += 1
        else:
            pitch.downvote +=1
        db.session.commit()
        return redirect('/home')

    return render_template('home.html', pitches = pitches)


