from app import db, app

def initialize_database():
    with app.app_context():
        db.create_all()
        print("Database initialized successfully.")

if __name__ == '__main__':
    initialize_database()
