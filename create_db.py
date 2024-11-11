from app import app, db

with app.app_context():
    db.create_all()  # Esto crea las tablas en PostgreSQL
