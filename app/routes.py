from app import app
from flask import render_template, flash, url_for, redirect
from app.forms import RegistrationForm

pitches = [
    {
        'author': 'James Dean',
        'title': 'Pitch 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018',
        'category' :'Technology'
    },
    {
        'author': 'Jane Doe',
        'title': 'Pitch 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018',
        'category': 'Biology'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pitches = pitches)

@app.route('/register', methods =['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)