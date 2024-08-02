
from db.init import (
    DataBaseConn,
    read_sql_script,
)

from src.logger.init import logger
from src.images.animal_request import AnimalClient
from src.images.cat import CatAPIAdapter
from src.images.dog import DogAPIAdapter


SOURCE = 'Init Project'

def initialize_db():
    logger.activity(SOURCE, 'INFO', 'Starting database conexion')
    db = DataBaseConn("./db/todo.db")

    logger.activity(SOURCE, 'INFO', 'Fetching data from database')
    sql_script = read_sql_script('db/StartDataScript.sql')
    data = db.fetch_query(sql_script)
    
    logger.activity(SOURCE, 'INFO', 'Database started...')
    return db, data

def image_generator():
    cat_api = CatAPIAdapter()
    dog_api = DogAPIAdapter()

    animal_client = AnimalClient([cat_api, dog_api])
    return animal_client

