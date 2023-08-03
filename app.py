from flask import Flask, request, jsonify
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import pickle
import joblib

# Load the model and the scaler
model = joblib.load('modeljb.joblib')
scaler = joblib.load('scaler.joblib')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! pakistan ....... zindabad'

@app.route('/predict', methods=['POST'])
def predict():

    Age = request.form.get('Age')
    Sex = request.form.get('Sex')
    RBC = request.form.get('RBC')     
    PCV = request.form.get('PCV')
    MCV = request.form.get('MCV')
    MCH = request.form.get('MCH')
    MCHC = request.form.get('MCHC')
    RDW = request.form.get('RDW')
    TLC = request.form.get('TLC')
    PLT = request.form.get('PLT')
    HGB = request.form.get('HGB')
    input_querry = np.array([[Age, Sex, RBC, PCV, MCV, MCH, MCH, RDW, TLC, PLT, HGB]])
    std_data1 = scaler.transform(input_querry)
    result = model.predict(std_data1)
    print(jsonify(str(result)))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"An error occurred: {e}")
