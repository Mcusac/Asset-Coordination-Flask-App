# app/__init__.py

import os
import pandas as pd
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assets.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    # Register blueprints
    from .admin import admin_bp
    from .user import user_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')

    # Define a root route
    @app.route('/')
    def home():
        return render_template('home.html')
    
    # Initialize the database and seed data
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        seed_data()      # Seed initial data if the table is empty

    return app

def seed_data():
    """Seeds the database with data from an Excel file if no records exist in the Asset table."""
    from .models import Asset

    if Asset.query.first() is None:  # Check if there is any data in the Asset table
        file_path = 'flask_app/Current ITR assets.xlsx'  # Path to your Excel file
        if os.path.exists(file_path):
            # Load only the first sheet, skip the title row if necessary
            data = pd.read_excel(file_path, sheet_name='Sheet1', header=1)  # Assumes headers start on the second row
            
            # Optional: Rename columns if they don’t match the database model exactly
            data.columns = [
                "business_unit", "asset_identification", "tag_number", "department",
                "serial_id", "description", "asset_status", "asset_profile_id",
                "location_code", "custodian_emplid", "custodian", "custodian_euid", "notes"
            ]

            # Iterate through each row in the DataFrame
            for _, row in data.iterrows():
                # Skip rows missing required fields like 'business_unit'
                if pd.isna(row.get('business_unit')):
                    print(f"Skipping row with missing business_unit: {row}")
                    continue

                # Create Asset object
                asset = Asset(
                    business_unit=row.get('business_unit'),
                    asset_identification=row.get('asset_identification'),
                    tag_number=row.get('tag_number'),
                    department=row.get('department'),
                    serial_id=row.get('serial_id'),
                    description=row.get('description'),
                    asset_status=row.get('asset_status'),
                    asset_profile_id=row.get('asset_profile_id'),
                    location_code=row.get('location_code'),
                    custodian_emplid=row.get('custodian_emplid'),
                    custodian=row.get('custodian'),
                    custodian_euid=row.get('custodian_euid'),
                    notes=row.get('notes')
                )
                db.session.add(asset)

            db.session.commit()
            print("Database seeded with data from Excel file.")
        else:
            print(f"Excel file '{file_path}' not found. No data was loaded.")

