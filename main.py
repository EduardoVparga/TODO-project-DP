from app.main import app

from init import (
    initialize_db
)

def main():

    # Start database  
    db, data = initialize_db()

    # Init application
    app(db, data)

if __name__ == "__main__":
    main()
