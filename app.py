# importing the dependencies
from flask import Flask, json, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create the sqlalchemy daatbase conncetion
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine,reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Hosting the flask app
app = Flask(__name__)

# define the welcome page
@app.route('/')
def welcome() : 
    return (
    '''
    Welcome to the Climate Analysis API!
    <br>Available Routes:
    <br>/api/v1.0/precipitation
    <br>/api/v1.0/stations
    <br>/api/v1.0/tobs
    <br>/api/v1.0/temp/start/end
    ''')

# display the precip page
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# define the stations page
@app.route("/api/v1.0/stations")
def stations() :
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations = stations)

# define the tobs page
@app.route("/api/v1.0/tobs")
def tobs():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)



# run the application
if __name__ == "__main__" : 
    app.run()
