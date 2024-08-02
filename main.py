from app.main import app

from init import (
    initialize_db,
    image_generator,
)


def main():
    
    # Start database  
    db, data = initialize_db()

    # Initialize imagen generator object
    animal_client = image_generator()

    # Init application
    app(db, data, animal_client)
    

if __name__ == '__main__':
    main()
