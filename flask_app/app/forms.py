# Form handling and validation
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Optional

# class AssetForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     location = StringField('Location', validators=[DataRequired()])
#     submit = SubmitField('Submit')

class UserUpdateRequestForm(FlaskForm):
    location_code = StringField("Location Code", validators=[Optional()])
    custodian = StringField("Custodian", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    submit = SubmitField("Request Update")

class AdminUpdateAssetForm(FlaskForm):
    # Add all fields with Optional validators for the admin update form
    business_unit = StringField("Business Unit", validators=[Optional()])
    asset_identification = StringField("Asset Identification", validators=[Optional()])
    tag_number = StringField("Tag Number", validators=[Optional()])
    department = StringField("Department", validators=[Optional()])
    serial_id = StringField("Serial ID", validators=[Optional()])
    description = StringField("Description", validators=[Optional()])
    asset_status = StringField("Asset Status", validators=[Optional()])
    asset_profile_id = StringField("Asset Profile ID", validators=[Optional()])
    location_code = StringField("Location Code", validators=[Optional()])
    custodian_emplid = StringField("Custodian Empl ID", validators=[Optional()])
    custodian = StringField("Custodian", validators=[Optional()])
    custodian_euid = StringField("Custodian EUID", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    submit = SubmitField("Update Asset")

class AddDeviceForm(FlaskForm):
    business_unit = StringField("Business Unit", validators=[Optional()])
    asset_identification = StringField("Asset Identification", validators=[Optional()])
    tag_number = StringField("Tag Number", validators=[DataRequired()])
    department = StringField("Department", validators=[Optional()])
    serial_id = StringField("Serial ID", validators=[Optional()])
    description = StringField("Description", validators=[Optional()])
    asset_status = StringField("Asset Status", validators=[Optional()])
    asset_profile_id = StringField("Asset Profile ID", validators=[Optional()])
    location_code = StringField("Location Code", validators=[Optional()])
    custodian_emplid = StringField("Custodian Empl ID", validators=[Optional()])
    custodian = StringField("Custodian", validators=[Optional()])
    custodian_euid = StringField("Custodian EUID", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])
    submit = SubmitField("Add Device")