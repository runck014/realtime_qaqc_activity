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

@app.route("/5572/milk_truck_sensor_geojson")
def milk_truck_sensor():
    '''
    Returns milk truck sensor data in GeoJSON format.
    Lat, lon, current time, and temperature sensor data are randomly nulled 5% of the API calls.
    '''
    
    # Generate location data
    lat = float(np.random.normal(46.7296, 1, 1)[0])
    lon = float(np.random.normal(-94, 1, 1)[0])
    
    # Generate timestamp
    now = datetime.now()
    current_time = now.strftime("%D:%H:%M:%S")
    
    # Generate temperature data
    air_temperature = float(np.random.normal(31, 15, 1)[0])
    
    # Randomly null data (5% chance for each)
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        air_temperature = None
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        # For GeoJSON, we'll keep coordinates but mark as null in properties
        has_valid_position = False
    else:
        has_valid_position = True
    
    if np.random.uniform(0.0, 1.0, 1)[0] < 0.05:
        current_time = None
    
    # Create properties object
    properties = {
        'current_time': current_time,
        'air_temperature': air_temperature,
        'has_valid_position': has_valid_position
    }
    
    # Create GeoJSON feature
    if has_valid_position:
        geojson = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [lon, lat]  # GeoJSON uses [longitude, latitude] order
            },
            'properties': properties
        }
    else:
        # If position is invalid, return null geometry
        geojson = {
            'type': 'Feature',
            'geometry': None,
            'properties': properties
        }
    
    # Add feature collection wrapper
    feature_collection = {
        'type': 'FeatureCollection',
        'features': [geojson]
    }
    
    return json.dumps(feature_collection, allow_nan=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
