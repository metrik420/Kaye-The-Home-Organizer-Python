from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import User
from app.extensions import db
from app.forms import ProfileForm

profile_bp = Blueprint('profile', __name__, template_folder='../templates')

@profile_bp.route('/profile/<int:user_id>', methods=['GET', 'POST'])
def profile(user_id):
    user = User.query.get(user_id)
    form = ProfileForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        flash('Profile updated successfully.')
        return redirect(url_for('profile.profile', user_id=user.id))
    return render_template('profile.html', form=form, user=user)

