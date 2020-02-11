import sqlalchemy as db
from sqlalchemy import create_engine, Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import OpenAPIWeather_new as openweather
import City 
from sqlalchemy.sql.expression import func
engine = db.create_engine('sqlite:///weather_w2.sqlite')

# Engine kreowanie silnika, memo sqlite baza tymczasowa
Base = declarative_base()


# Zwrócenie wartości z API  



class Weather(Base):
    __tablename__ ='weather'
    id = Column(Integer,primary_key=True)
    location_id = Column(Integer)
    wind_id = Column(Integer)
    temperature= Column(Float)
    humidity= Column(Float) 

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    lon  = Column(Integer)
    lat  = Column(Integer) 

class Wind(Base):
    __tablename__ = 'wind' 
    id = Column(Integer,primary_key=True)
    speed = Column(Float)
    deg = Column(Integer)
# Getting data index from database
# Sesja napisanie pierwszej przykładowej kwerendy
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


'''
# Base metadata tworzymy nowe tabelę
maxid = session.query(func.max(Wind.id))
maxid =int(0 if maxid.scalar() is None else maxid.scalar())+1
london_weather = Weather(id=maxid,location_id=264,wind_id=1,temperature=26.0,humidity=5.4)
london = City(id=2555555,name ='London',lat=41,lon=57)
london_wind = Wind(id=maxid,speed=3.9,deg=10)
'''
def add_city_to_database(number_of_cities):
    cityid = city.citiesid(number_of_cities)
    # Sprawdzamy czy cityid istnieje w bazie danych w tabeli London jeżeli nie istnieje wówczas
    # dodajemy nowe city 
    new_cityid =[c for c in cityid if c not in session.query(City.id)]
    for id in new_cityid:
        #weather_data = Weather_Data(id)
        #wind_data = Wind_Data(id)
        city_data = City_Data(id)
        session.add(city_data)
        session.commit()
# First add city 
def wind_weather_to_database():
    for cid in session.query(City.id):
        # Add weather, wind to database
        maxweather_id = session.query(func.max(Weather.id))
        maxwind_id = session.query(func.max(Wind.id))
        weather_data = Weather_Data(cid)
        wind_data = Wind_Data(cid)
        city_weather = Weather(id = maxweather_id,location_id = cid, wind_id = maxwind_id, temperature = city_weather.temp, humidity = city_weather.humidity)
        city_wind = Wind(id = maxwind_id,speed = wind_data.speed,deg = wind_data.deg)
        session.add(city_weather)
        session.add(city_wind)
        session.commit()

'''
#session.add(london_weather)
session.add(london)
session.query(City).filter(City.id == london.id).delete()
session.add(london_wind)
session.commit()
for instance in  session.query(Weather):
    print(instance.id,instance.temperature,instance.humidity)
#for wind in session.query(Wind):
#    print(wind.id,wind.speed,wind.deg)
'''
