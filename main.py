import os
import sqlalchemy
import numpy as np
from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    matrix = np.random.rand(3,2)
    return str(matrix)


@app.route("/hello")
def hello():
    return "hello"


@app.route("/5572/milk_truck_sensor")
def milk_truck_sensor():
    '''
    Returns lat, lon, current time, and temperature sensor.
    All are randomly nulled 5% of the API calls.
    '''
    
    lat = float(np.random.normal(46.7296, 1, 1)[0])
    lon = float(np.random.normal(-94, 1, 1)[0])
    
    now = datetime.now()
    current_time = now.strftime("%D:%H:%M:%S")
    
    air_temperature = float(np.random.normal(31, 15, 1)[0])
    
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        air_temperature = None
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        lat = None
        
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        lon = None
    
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        current_time = '01/21/29:15:11:12'
    
    response_dict = {
        'lat': lat,
        'lon': lon,
        'current_time': current_time,
        'air_temperature': air_temperature
    }
    
    return json.dumps(response_dict, allow_nan=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
