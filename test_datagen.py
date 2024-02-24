import unittest
import pandas as pd
import os
from Dataset_gen import generate_initial_data, generate_sensor_data

class TestSensorScript(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.test_file_name = "test_sensor_data.csv"
        self.test_data_points = 10
        generate_initial_data(self.test_file_name, self.test_data_points)

    def test_generate_initial_data(self):
        # Check if file is created
        self.assertTrue(os.path.exists(self.test_file_name))

        # Read the test file
        test_data = pd.read_csv(self.test_file_name)

        # Check if the number of data points matches
        self.assertEqual(len(test_data), self.test_data_points)

        # Check if columns are present
        expected_columns = ['Date', 'Time', 'Temperature', 'Sound', 'Humidity']
        self.assertListEqual(list(test_data.columns), expected_columns)

    def test_generate_sensor_data(self):
          
          # Check if file is created
          self.assertTrue(os.path.exists('sensor_data.csv'))
          
          # Read the test file
          test_data = pd.read_csv('sensor_data.csv')
          
          # Check if columns are present
          expected_columns = ['Date', 'Time', 'Temperature', 'Sound', 'Humidity']
          self.assertListEqual(list(test_data.columns), expected_columns)


    def tearDown(self):
        # Clean up test files after tests are done
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

if __name__ == '__main__':
    unittest.main()