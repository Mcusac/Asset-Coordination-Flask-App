# app/user/routes.py

from flask import render_template, redirect, url_for, flash
from . import user_bp
from ..models import Asset, UpdateRequest
from ..forms import UserUpdateRequestForm
from .. import db

@user_bp.route('/')
def user_dashboard():
    assets = Asset.query.all()  # Fetch all assets
    return render_template('user/dashboard.html', assets=assets)

# submit an update request to an admin
@user_bp.route('/asset/<int:asset_id>/request_update', methods=['GET', 'POST'])
def request_update(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    form = UserUpdateRequestForm()
    if form.validate_on_submit():
        requested_changes = {
            "location_code": form.location_code.data,
            "custodian": form.custodian.data,
            "notes": form.notes.data,
        }
        # Create a new update request with the requested changes
        update_request = UpdateRequest(
            asset_id=asset_id,
            requested_changes=str(requested_changes),  # Serialize to string or JSON if needed
        )
        db.session.add(update_request)
        db.session.commit()
        flash('Update request submitted successfully.', 'success')
        return redirect(url_for('user.user_dashboard'))  # Adjust to your dashboard route
    return render_template('user/request_update.html', form=form, asset=asset)