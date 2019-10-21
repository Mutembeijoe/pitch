from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '27680ccbcade6026e338d4349503c3ad'

from app import routes