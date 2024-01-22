import numpy as np
import pandas as pd
import time

#creating synthetic dataset for sensor temperature, humidity and sound volume
num_samples = 1000
time_intervals = np.arange(num_samples)
update_interval = 30 #Time interval between each update in seconds

while True:
          #creating random values for temperature, humidity and sound volume
          temperature = np.random.normal(25, 5, num_samples)
          humidity = np.random.normal(50, 10, num_samples)
          sound_volume = np.random.normal(30, 50, num_samples)

          #creating pandas dataframe with columns for each sensor dataset
          data = ({'Time': time_intervals,  
                    'Temperature': temperature, 
                    'Humidity': humidity, 
                    'Sound Volume': sound_volume})
          
          df = pd.DataFrame(data)
          

          #sleeping for 30 seconds before next update
          time.sleep(update_interval)

          print(df.head())


