import os 
import sys 
import sqlalchemy as db
# Import SessionMarker to ORM 
from sqlalchemy.orm import sessionmaker
# Create database for weather data 
engine = db.create_engine('sqlite:///weather.sqlite')
connection = engine.connect()
metadata = db.MetaData()

# Creating session to query data
Session = sessionmaker(bind=engine)
session = Session()

# Create table weather 
weather = db.Table(
    'weather',metadata,
    db.Column('id',db.Integer,primary_key =True),
    db.Column('cityid',db.Integer),
    db.Column('temperature',db.String),
    db.Column('humility',db.String),
)
metadata.create_all(engine)
# Pobieramy glowne id do zmiennej i aktualizujemy ją o 1 
s = weather.select()
weather_id = session.query(weather.id)
all_ids = weather_id.all()
result = engine.execute(s)
print(s)
for row in result:
    print(row)
# Insertujemy pierwsze przykładowe dane do naszej nowej tabeli
#ins = weather.insert().values(id =1)
# Commitujemy naszą zmianę do tabeli
#result = connection.execute(ins)
