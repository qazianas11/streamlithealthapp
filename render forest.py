import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score

# Load the dataset into a DataFrame
data = pd.read_csv("C:\MinGW\c++\.vscode\mixed_values.csv")

# Drop rows with missing values
data = data.dropna()

# Separate the features (X) and target variable (y)
X = data.drop("Result", axis=1)  # Adjust the column name if necessary
y = data["Result"]  # Adjust the column name if necessary

# Identify categorical and numerical columns
categorical_cols = ['Gender of the patient']  # Add other categorical columns if any
numerical_cols = ['Age of the patient', 'Total Bilirubin', 'Direct Bilirubin', 'Alkphos Alkaline Phosphotase', 'Sgpt Alamine Aminotransferase', 'Sgot Aspartate Aminotransferase', 'Total Protiens', 'ALB Albumin', 'A/G Ratio Albumin and Globulin Ratio']  # Add other numerical columns if any

# Create the column transformer for encoding and scaling
preprocessor = ColumnTransformer([
    ('encoder', OneHotEncoder(), categorical_cols),
    ('scaler', StandardScaler(), numerical_cols)
])

# Apply preprocessing on the feature columns
X_encoded = preprocessor.fit_transform(X)

# Split the preprocessed data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
random_forest = RandomForestClassifier()

# Fit the classifier to the training data
random_forest.fit(X_train, y_train)


# Get the feature importances (weights) of the Random Forest model
feature_importances = random_forest.feature_importances_

# Save the feature importances to a file
np.save("feature_importances.npy", feature_importances)

# Make predictions on the testing data
predictions = random_forest.predict(X_test)

if predictions[0]==1:
    print("Positive case")
else:
    print("Negative case")






import joblib

# ...

#Save the trained Random Forest model
joblib.dump(random_forest, 'random_forest_model.joblib')






