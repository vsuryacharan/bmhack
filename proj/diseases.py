import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
data = pd.read_csv('symptoms_data.csv')

# Fill missing values
data.fillna('No Symptom', inplace=True)

# One-hot encode the data
data_encoded = pd.get_dummies(data, columns=data.columns[1:], drop_first=True)

# Split data into features (X) and target (y)
X = data_encoded.drop('Disease', axis=1)
y = data_encoded['Disease']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

