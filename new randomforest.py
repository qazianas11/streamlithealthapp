# Import the necessary libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load the dataset into a DataFrame
data = pd.read_csv("C:\MinGW\c++\.vscode\cleaned_dataset 14k.csv")

# Drop rows with missing values
data = data.dropna()

# Separate the features (X) and target variable (y)
X = data.drop("Result", axis=1)
y = data["Result"]

# Identify categorical and numerical columns
categorical_cols = ['Gender of the patient']
numerical_cols = ['Age of the patient', 'Total Bilirubin', 'Direct Bilirubin', 'Alkphos Alkaline Phosphotase', 'Sgpt Alamine Aminotransferase', 'Sgot Aspartate Aminotransferase', 'Total Protiens', 'ALB Albumin', 'A/G Ratio Albumin and Globulin Ratio']

# Create the column transformer for encoding and scaling
preprocessor = ColumnTransformer([
    ('encoder', OneHotEncoder(), categorical_cols),
    ('scaler', StandardScaler(), numerical_cols)
])

# Apply preprocessing on the feature columns
X_encoded = preprocessor.fit_transform(X)

# Initialize the Random Forest classifier
random_forest = RandomForestClassifier()

# Fit the classifier to the data
random_forest.fit(X_encoded, y)

# Define the class labels dictionary
class_labels = {0: 'Negative', 1: 'Positive', 2: 'Normal'}

# Create a new DataFrame with the data for a single sample
new_data = pd.DataFrame({
    'Age of the patient': [user_input['age']],  # Replace 'user_input['age']' with the actual user input for age
    'Total Bilirubin': [user_input['total_bilirubin']],  # Replace 'user_input['total_bilirubin']' with the actual user input for total bilirubin
    'Direct Bilirubin': [user_input['direct_bilirubin']],  # Replace 'user_input['direct_bilirubin']' with the actual user input for direct bilirubin
    'Alkphos Alkaline Phosphotase': [user_input['alkphos']],  # Replace 'user_input['alkphos']' with the actual user input for alkphos
    'Sgpt Alamine Aminotransferase': [user_input['sgpt']],  # Replace 'user_input['sgpt']' with the actual user input for sgpt
    'Sgot Aspartate Aminotransferase': [user_input['sgot']],  # Replace 'user_input['sgot']' with the actual user input for sgot
    'Total Protiens': [user_input['total_proteins']],  # Replace 'user_input['total_proteins']' with the actual user input for total proteins
    'ALB Albumin': [user_input['albumin']],  # Replace 'user_input['albumin']' with the actual user input for albumin
    'A/G Ratio Albumin and Globulin Ratio': [user_input['ag_ratio']],  # Replace 'user_input['ag_ratio']' with the actual user input for A/G ratio
    'Gender of the patient': [user_input['gender']]  # Replace 'user_input['gender']' with the actual user input for gender, make sure to encode categorical variables properly
})

# Apply preprocessing on the new data
new_data_encoded = preprocessor.transform(new_data)

# Make a single prediction on the new data
prediction = random_forest.predict(new_data_encoded)

# Convert the predicted label to the corresponding class value
predicted_label = class_labels[prediction[0]]

# Print the predicted label
print('Predicted Label:', predicted_label)



# Create a new DataFrame with the data for a single sample
new_data = pd.DataFrame({
    'Age of the patient': [30],  # Replace with appropriate user input from Flutter
    'Total Bilirubin': [_bilirubinController.text],  # Replace with _bilirubinController.text from Flutter
    'Direct Bilirubin': [_dbController.text],  # Replace with _dbController.text from Flutter
    'Alkphos Alkaline Phosphotase': [_alkphosController.text],  # Replace with _alkphosController.text from Flutter
    'Sgpt Alamine Aminotransferase': [_sgptController.text],  # Replace with _sgptController.text from Flutter
    'Sgot Aspartate Aminotransferase': [_sgotController.text],  # Replace with _sgotController.text from Flutter
    'Total Protiens': [tpController.text],  # Replace with tpController.text from Flutter
    'ALB Albumin': [3.8],  # Replace with appropriate user input from Flutter
    'A/G Ratio Albumin and Globulin Ratio': [agRatioController.text],  # Replace with agRatioController.text from Flutter
    'Gender of the patient': ['Male']  # Replace with appropriate user input from Flutter
})


# Define the class labels dictionary
class_labels = {0: 'Negative', 1: 'Positive', 2: 'Normal'}

# Create a new DataFrame with the data for a single sample
new_data = pd.DataFrame({
    'Age of the patient': [30],
    'Total Bilirubin': [0.8],
    'Direct Bilirubin': [0.2],
    'Alkphos Alkaline Phosphotase': [150],
    'Sgpt Alamine Aminotransferase': [50],
    'Sgot Aspartate Aminotransferase': [40],
    'Total Protiens': [6.4],
    'ALB Albumin': [3.8],
    'A/G Ratio Albumin and Globulin Ratio': [1.2],
    'Gender of the patient': ['Male']  # Make sure to encode categorical variables properly
})

# Apply preprocessing on the new data
new_data_encoded = preprocessor.transform(new_data)

# Make a single prediction on the new data
prediction = random_forest.predict(new_data_encoded)

# Convert the predicted label to the corresponding class value
predicted_label = class_labels[prediction[0]]

# Print the predicted label
print('Predicted Label:', predicted_label)


