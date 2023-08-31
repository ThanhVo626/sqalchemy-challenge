# Import the dependencies.
import flask
from flask import Flask,jsonify

import pandas as pd
import numpy as np
import datetime as dt


from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func, inspect


#################################################
# Database Setup
#################################################
engine =create_engine('sqlite:///Resources/hawaii.sqlite')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
             
#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return(f'Routes to choose from' 
            f'/api/v1.0/precipitation'
            f'/api/v1.0/stations')


@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    p = session.query(measurement.prcp,measurement.date).filter(measurement.date > '2016-08-23').order_by(measurement.date).all()
    session.close()
    pdict = {}
    for prcp, date in p:
        pdict[date] = prcp
    return jsonify(pdict)
@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    s = session.query(Station.station).all()
    session.close()
    slist = list(np.ravel(s))
    return jsonify(slist)
@app.route('/api/v1.0/tobs')
def tobs():
    session = Session(engine)
    temp = session.query(measurement.tobs,measurement.date).filter(measurement.date>'2016-08-23',measurement.station == 'USC00519281').order_by(measurement.date).all()
    session.close()
    tdict = {}
    for t, date in temp:
        tdict[date] = t
    return jsonify(tdict)
@app.route('/api/v1.0/<startdate>')
def start_date(startdate):
    session = Session(engine)
    low = list(np.ravel(session.query(func.min(measurement.tobs).filter(measurement.date >= startdate)).all()))
    avg = list(np.ravel(session.query(func.avg(measurement.tobs).filter(measurement.date >= startdate)).all()))
    high = list(np.ravel(session.query(func.max(measurement.tobs).filter(measurement.date >= startdate)).all()))
    session.close()
    return jsonify(f'The min temp is {low}, The max temp is {high}, The average temp is {avg}')

@app.route('/api/v1.0/<start>/<end>')
def start_end(start,end):
    session = Session(engine)
    low = list(np.ravel(session.query(func.min(measurement.tobs).filter(measurement.date >= start).filter(measurement.date <= end)).all()))
    avg = list(np.ravel(session.query(func.avg(measurement.tobs).filter(measurement.date >= start).filter(measurement.date <= end)).all()))
    high = list(np.ravel(session.query(func.max(measurement.tobs).filter(measurement.date >= start).filter(measurement.date <= end)).all()))
    session.close()
    return jsonify(f'The min temp is {low}, The max temp is {high}, The average temp is {avg}')

if __name__ == '__main__':
    app.run(debug=True)

