# app/models.py

from . import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_unit = db.Column(db.String(50))
    asset_identification = db.Column(db.String(50))
    tag_number = db.Column(db.String(50))
    department = db.Column(db.String(50))
    serial_id = db.Column(db.String(50))
    description = db.Column(db.String(200))
    asset_status = db.Column(db.String(50))
    asset_profile_id = db.Column(db.String(50))
    location_code = db.Column(db.String(50))
    custodian_emplid = db.Column(db.String(50))
    custodian = db.Column(db.String(50))
    custodian_euid = db.Column(db.String(50))
    notes = db.Column(db.Text)

    # Add the relationship to UpdateRequest with back_populates
    update_requests = db.relationship('UpdateRequest', back_populates='asset', cascade="all, delete-orphan")

class UpdateRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('asset.id'), nullable=False)
    requested_changes = db.Column(db.JSON)  # Store requested changes as JSON
    status = db.Column(db.String(20), default="Pending")

    # Relationship back to the asset
    asset = db.relationship('Asset', back_populates='update_requests')
