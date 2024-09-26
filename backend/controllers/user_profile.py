import requests
from flask import Blueprint, render_template, flash
from flask_login import current_user
from werkzeug.security import generate_password_hash
from backend.extensions import db
from backend.models.forms.user_profile_form import UserProfileForm
from backend.models.model_user import User

user_profile_bp = Blueprint('user_profile', __name__)


@user_profile_bp.route('/my-profile', methods=['GET', 'POST'])
def index():
    user = User.get_user(current_user.id)
    form = UserProfileForm(obj=current_user)
    disclaimer = 'Your request to change your authorization level will be sent to a user with a high authorization level for approval.'
    show_disclaimer = False
    if user:
        if form.validate_on_submit():
            current_user.email = form.data['email']
            current_user.password = generate_password_hash(form.data['password'])
            if form.data["auth_level"] != user['auth_level']:
                show_disclaimer = True
            db.session.commit()
    return render_template("user_profile.html", form=form, show_disclaimer=show_disclaimer, disclaimer=disclaimer)
