from database import models, database

models.metadata.create_all(database)