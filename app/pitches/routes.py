from flask import Blueprint, flash, url_for, render_template, redirect
from flask_login import login_required, current_user

from app import db
from app.models import Pitch
from app.pitches.forms import PitchForm

pitches = Blueprint('pitches', __name__)


@pitches.route('/pitch/new', methods =['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, content=form.content.data, category= form.category.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_pitch.html', form = form)