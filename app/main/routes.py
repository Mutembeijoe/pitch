from flask import Blueprint


main = Blueprint('main',__name__)

@app.route('/')
@app.route('/home')
def home():
    pitches = Pitch.query.all()
    return render_template('home.html', pitches = pitches)


