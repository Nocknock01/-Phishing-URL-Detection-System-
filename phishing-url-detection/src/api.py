# src/api.py
from flask import Flask, request, jsonify
import joblib
from features import url_features, extract_tokens
from scipy.sparse import hstack
import numpy as np


app = Flask(__name__)
obj = joblib.load('models/rf_model.joblib')
model = obj['model']
vectorizer = obj['vectorizer']




@app.route('/predict', methods=['POST'])
def predict():
data = request.json
if not data or 'url' not in data:
return jsonify({'error': 'no url provided'}), 400
url = data['url']
feats = url_features(url)
num = np.array([list(feats.values())])
token = ' '.join(extract_tokens(url))
x_text = vectorizer.transform([token])
X = hstack([num, x_text])
pred = int(model.predict(X)[0])
prob = float(model.predict_proba(X)[0][1]) if hasattr(model, 'predict_proba') else None
return jsonify({'url': url, 'phishing': bool(pred), 'probability': prob})




if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)