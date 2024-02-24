from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('model_IF.pkl', 'rb'))

@app.route('/predict', methods=['POST'])

def predict():
          # Get the data from the POST request.
          data = request.get_json(force=True)
          df = pd.DataFrame(data, index=[0])
          
          # Make prediction using the model
          prediction = model.predict(df[['Temperature', 'Sound', 'Humidity']])
          
          # Take the first value of prediction
          output = {'anomaly_score': int(prediction[0]), 'Anomaly or Normal': 'Yes' if prediction[0] == -1 else 'Normal'}
          return jsonify(output)

if __name__ == '__main__':
          app.run(host='0.0.0.0', port=5000)