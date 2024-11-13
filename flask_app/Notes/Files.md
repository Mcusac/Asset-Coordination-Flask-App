flask_app/
├── app/
│   ├── __init__.py                # Initializes the Flask app and blueprints
│   ├── models.py                  # Defines database models (e.g., Asset)
│   ├── forms.py                   # Defines Flask-WTF forms (e.g., UpdateRequestForm)
│   │
│   ├── admin/                     # Admin blueprint folder
│   │   ├── __init__.py            # Initializes the admin blueprint
│   │   ├── routes.py              # Routes for admin functionalities (e.g., view_assets)
│   │
│   ├── user/                      # User blueprint folder
│   │   ├── __init__.py            # Initializes the user blueprint
│   │   ├── routes.py              # Routes for user functionalities (e.g., user_dashboard, request_update)
│   │
│   ├── templates/
│   │   ├── base.html              # Base template with shared HTML structure
│   │   ├── home.html              # Home page template
│   │
│   │   ├── admin/
│   │   │   ├── assets.html        # Template for displaying asset list in admin view
│   │   │   ├── update_asset.html  # Template for admin updating asset details
│   │
│   │   ├── user/
│   │       ├── dashboard.html     # Template for user dashboard displaying assets
│   │       ├── request_update.html# Template for user to request asset update
│   │
├── app/
│   ├── assets.db                  # SQLite database file
│   │
├── migrations/                    # Database migrations folder (if using Flask-Migrate)
├── Current ITR assets.xlsx        # Excel file for initial asset data
├── run.py                         # Run file to start the Flask application
├── test.py                        # Test run the app
├── ReadMe                         # ReadMe file
