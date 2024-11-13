# test_data.py
from app import create_app, db
from app.models import Asset

app = create_app()
with app.app_context():
    assets = Asset.query.all()
    print("Assets in Database:", assets)

print(app.url_map)  # This will list all registered routes in the application
