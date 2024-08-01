
from db.init import (
    DataBaseConn,
    read_sql_script,
)





def initialize_db():
    db = DataBaseConn("./db/todo.db")

    sql_script = read_sql_script('db/StartDataScript.sql')
    data = db.fetch_query(sql_script)
    
    return db, data


