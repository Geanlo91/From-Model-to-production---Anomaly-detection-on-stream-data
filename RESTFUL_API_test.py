import requests
import pandas as pd
import time



# URL of the FLASK API
url = 'http://localhost:5000/predict'

while True:
    # Load the most recent data from sensor data csv
    sensor_data = pd.read_csv('sensor_data.csv')
    
    # Select the last row of the DataFrame
    last_row = sensor_data.iloc[-1].to_dict()
    
    # Send a POST request to the API with the last row of data
    response = requests.post(url, json=last_row)
    
    # Print the response
    print(response.text)
    
    # Wait for 1 second before the next iteration to align with the update frequency
    time.sleep(1)