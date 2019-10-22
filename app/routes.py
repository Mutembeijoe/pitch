from app import app, bcrypt, db
from flask import render_template, flash, url_for, redirect, request, current_app
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PitchForm, CommentForm
from flask_login import login_user,current_user, logout_user, login_required
from app.models import User, Pitch, Comment
import secrets, os
from PIL import Image





