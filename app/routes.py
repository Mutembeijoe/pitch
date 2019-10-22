from app import app
from flask import render_template, flash, url_for, redirect
from app.forms import RegistrationForm, LoginForm

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
