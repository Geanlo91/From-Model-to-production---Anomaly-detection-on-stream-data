
import pandas as pd
import time
import random
from datetime import datetime

def generate_initial_data(file_name, data_points=1000):
    columns = ['Date', 'Time', 'Temperature', 'Sound', 'Humidity']
    data_initial = pd.DataFrame(columns=columns)
    
    for _ in range(data_points):
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')
        if random.random() < 0.10:  # 10% chance of generating an anomaly
            temperature = random.uniform(10, 40)
            sound = random.uniform(30, 100)
            humidity = random.uniform(20, 80)
        else:
            temperature = random.uniform(20, 30)
            sound = random.uniform(50, 70)
            humidity = random.uniform(40, 60)
            
        new_row = pd.DataFrame([[date, time_str, temperature, sound, humidity]], columns=columns)
        data_initial = pd.concat([data_initial, new_row], ignore_index=True)
    
    data_initial.to_csv(file_name, index=False)
    

# Generate initial data
generate_initial_data("initial_sensor_data.csv")


def generate_sensor_data():
    # Initialize an empty DataFrame with the specified columns
    columns = ['Date', 'Time', 'Temperature', 'Sound', 'Humidity']
    data_df = pd.DataFrame(columns=columns)

    while True:
        # Get the current date and time
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        time_str = now.strftime('%H:%M:%S')

        # Determine if this is an anomaly or regular data
        if random.random() < 0.10:  # 5% chance of generating an anomaly
            temperature = random.uniform(10, 45)
            sound = random.uniform(30, 90)
            humidity = random.uniform(20, 60)
        else:
            temperature = random.uniform(25, 30)
            sound = random.uniform(50, 65)
            humidity = random.uniform(35, 60)

        # Create a new row of data
        new_row = pd.DataFrame([[date, time_str, temperature, sound, humidity]], columns=columns)

        # Append new data, remove the oldest if more than 1000
        if len(data_df) >= 1000:
 
            data_df = pd.concat([data_df.iloc[1:], new_row], ignore_index=True)
        else:
            data_df = pd.concat([data_df, new_row], ignore_index=True)
        # Write the DataFrame to the file, replacing its contents
        with open("sensor_data.csv", "w") as file:
            file.write(data_df.to_csv(index=False))
            print(data_df)


        # Wait for 1 second
        time.sleep(1)


# Call the function to start generating data
generate_sensor_data()









        



