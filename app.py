import sqlalchemy
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

#Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to 'Home' page!<br/>"
        f"Here are the list of API's:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation data for last year"""
    # Calculate date a year ago from last date
    prev_year = dt.date(2017,8,23)-dt.timedelta(days=365)

    # Query date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp)\
                 .filter(Measurement.date>prev_year).all()

    session.close()
    # This is a dictionary with the date as a key, prcp is a value             
    precipitation_dict = {date:prcp for date, prcp in precipitation}
    return jsonify(precipitation_dict)





@app.route("/api/v1.0/stations")    
def stations():
    """Return a list of stations"""
    results = session.query(Station.station).all()

    session.close()

    # Unravel results into a 1D array and convert to a list
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

if __name__ == '__main__':
    app.run()         