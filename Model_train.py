import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import classification_report

# Load the data
data_initial = pd.read_csv('initial_sensor_data.csv')

# Split data into training and testing
train_df, test_df = train_test_split(data_initial, test_size=0.5, random_state=1000)

# Load the validation data
data_df = pd.read_csv('sensor_data.csv')

# Create Isolation forest model
anomaly_inputs = train_df[['Temperature', 'Sound', 'Humidity']].values
model_IF = IsolationForest(contamination=0.10,n_estimators=30, random_state=42, max_features=3, max_samples=100)

# Train the model
model_IF.fit(anomaly_inputs)

# Predict anomalies on training data
train_df['anomaly_score'] = model_IF.decision_function(anomaly_inputs)
train_df['outlier'] = model_IF.predict(anomaly_inputs)


# Visualize the anomaly scores
plt.figure(figsize=(10, 6))
sns.displot(train_df['anomaly_score'], bins=50, kde=True)
plt.title('Distribution of Anomaly Scores')
plt.show()

# Save the model
pickle.dump(model_IF, open('model_IF.pkl', 'wb'))

#Test the model using the test data
test_inputs = test_df[['Temperature', 'Sound', 'Humidity']].values
test_df['anomaly_score'] = model_IF.decision_function(test_inputs)
test_df['outlier'] = model_IF.predict(test_inputs)
#calculate accuracy of the model in percentage based on anomalies and non-anomalies
test_accuracy = (test_df['outlier'].value_counts().iloc[0]/len(test_df['outlier']))
print("Test Accuracy: ", test_accuracy)


# Prepare validation data
validation_inputs = data_df[['Temperature', 'Sound', 'Humidity']].values

# Predict anomalies on validation data
data_df['anomaly_score'] = model_IF.decision_function(validation_inputs)
data_df['outlier'] = model_IF.predict(validation_inputs)

# Define a function to plot the data
def plot_anomaly(df, col1, col2, col3):
    fig, axs = plt.subplots(3, 1, figsize=(15, 7))
    for i, col in enumerate([col1, col2, col3]):
        axs[i].plot(df[col], color='blue' if i == 0 else 'green' if i == 1 else 'red')
        axs[i].set_title(col)
    plt.tight_layout()
    plt.show()

# Use seaborn to plot the distribution of outliers
palette = {1: 'blue', -1: 'red'}
sns.pairplot(data_df[['Temperature', 'Sound', 'Humidity', 'outlier']], hue='outlier', palette=palette)
plt.show()

#print count of the anomalies
print(data_df['outlier'].value_counts())
#calculate accuracy of the model in percentage based on anomalies and non-anomalies
accuracy = (data_df['outlier'].value_counts().iloc[0]/len(data_df['outlier']))
print("Model Accuracy: ", accuracy)



   


