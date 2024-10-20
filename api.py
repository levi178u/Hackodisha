
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('xgb_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_features = pd.DataFrame(data)

    predictions = model.predict(input_features)
    probabilities = model.predict_proba(input_features)[:, 1]

    response = {
        'predictions': predictions.tolist(),
        'probabilities': probabilities.tolist()
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
