from flask import Blueprint, flash, url_for, redirect, render_template
from flask_login import login_required, current_user


from app.comments.forms import CommentForm
from app.models import Comment
from app import db

comments = Blueprint('comments', __name__)

@comments.route('/add_comment/<int:pitch_id>', methods = ['GET', 'POST'])
@login_required
def add_comment(pitch_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(pitch_id = pitch_id, description =form.description.data,
                      author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment was added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_comment.html', form=form)

