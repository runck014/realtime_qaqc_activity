# Real-time QAQC Class Activity 

This app provides the milk truck sensor endpoint in main.py for deployment on Google Cloud Run.

# Activity
An air temperature sensor is on a dairy truck driving around Minnesota. Air temperature helps the fleet operator understand the risk of milk spoilage (because milk trucks aren’t refrigerated).

The sensors can be queried on demand from here: <link>

Your job is to build a QAQC pipeline in a Jupyter Notebook for the <x,y,t,val> tuple stream from the sensor. Focus on cleaning outliers and missing data.

**Consider**
- How will you repeatedly sample the data? 
- Please use time.sleep(.1) so you don’t flood the API)
- How will you approach the problem?
- Where will you save the data?
- How will you define “outlier” for each parameter?
- The truck only moves in Minnesota. Geofencing?
- Air temperature is on average 31 degrees for the time of year
- What percentage of packets have errors?

In your code
- For each QAQC function / operation, label it with a comment. 

After you finish writing the code, draw a diagram of the QAQC workflow 


