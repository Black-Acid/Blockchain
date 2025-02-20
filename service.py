import database as db
import fastapi


def create_db():
    db.Base.metadata.create_all(bind=db.engine)
    
    
def get_db():
    database = db.sessionLocal()
    
    try: 
        yield database
    finally:
        database.close
    