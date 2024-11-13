# app/admin/routes.py

from flask import render_template, redirect, url_for, flash
from ..models import Asset, UpdateRequest
from .. import db  # Import db from the app package
from ..forms import AddDeviceForm, AdminUpdateAssetForm  # Import the necessary forms
from . import admin_bp  # Import the already-initialized blueprint

@admin_bp.route('/assets')
def view_assets():
    assets = Asset.query.all()
    return render_template('admin/assets.html', assets=assets)

# Admin Asset Update
@admin_bp.route('/asset/<int:asset_id>/update', methods=['GET', 'POST'])
def update_asset(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    form = AdminUpdateAssetForm(obj=asset)
    if form.validate_on_submit():
        # Only update fields if they are not empty
        for field_name, field in form._fields.items():
            if field.data:
                setattr(asset, field_name, field.data)
        db.session.commit()
        flash('Asset updated successfully.', 'success')
        return redirect(url_for('admin.view_assets'))
    return render_template('admin/update_asset.html', form=form, asset=asset)

# Add device to list
@admin_bp.route('/add_device', methods=['GET', 'POST'])
def add_device():
    form = AddDeviceForm()
    if form.validate_on_submit():
        # Create a new Asset object with form data
        new_asset = Asset(
            tag_number=form.tag_number.data,
            description=form.description.data,
            department=form.department.data,
            asset_status=form.asset_status.data,
            location_code=form.location_code.data,
            custodian=form.custodian.data,
            asset_identification=form.asset_identification.data,
            serial_id=form.serial_id.data,
            business_unit=form.business_unit.data,
            notes=form.notes.data  # Add notes field if applicable
        )
        db.session.add(new_asset)
        db.session.commit()
        flash('New device added successfully.', 'success')
        return redirect(url_for('admin.view_assets'))
    return render_template('admin/add_device.html', form=form)

# Delete/Remove device from list
@admin_bp.route('/asset/<int:asset_id>/delete', methods=['POST'])
def delete_asset(asset_id):
    asset = Asset.query.get_or_404(asset_id)
    db.session.delete(asset)
    db.session.commit()
    flash('Device successfully deleted.', 'success')
    return redirect(url_for('admin.view_assets'))

# Admin Dashboard
@admin_bp.route('/dashboard')
def admin_dashboard():
    # Retrieve all pending update requests
    update_requests = UpdateRequest.query.filter_by(status="Pending").all()
    return render_template('admin/dashboard.html', update_requests=update_requests)

# Approve request
@admin_bp.route('/update_request/<int:request_id>/approve', methods=['POST'])
def approve_request(request_id):
    update_request = UpdateRequest.query.get_or_404(request_id)
    asset = update_request.asset

    # Update asset fields based on requested changes
    changes = update_request.requested_changes
    for field, value in changes.items():
        if hasattr(asset, field):
            setattr(asset, field, value)

    # Commit the updates and mark the request as approved
    db.session.commit()
    update_request.status = "Approved"
    db.session.commit()
    flash("Request approved and asset updated successfully.", "success")
    return redirect(url_for('admin.admin_dashboard'))

# Deny request
@admin_bp.route('/update_request/<int:request_id>/deny', methods=['POST'])
def deny_request(request_id):
    update_request = UpdateRequest.query.get_or_404(request_id)
    update_request.status = "Denied"
    db.session.commit()
    flash("Request denied.", "danger")
    return redirect(url_for('admin.admin_dashboard'))