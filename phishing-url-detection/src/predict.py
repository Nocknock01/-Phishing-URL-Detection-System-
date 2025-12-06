# src/predict.py
import joblib
import sys
from features import url_features, extract_tokens
from scipy.sparse import hstack
import numpy as np


MODEL_PATH = 'models/rf_model.joblib'




def predict_single(url):
obj = joblib.load(MODEL_PATH)
model = obj['model']
vectorizer = obj['vectorizer']


feats = url_features(url)
num = np.array([list(feats.values())])
token = ' '.join(extract_tokens(url))
x_text = vectorizer.transform([token])
from scipy.sparse import hstack
X = hstack([num, x_text])
pred = model.predict(X)
return int(pred[0])




if __name__ == '__main__':
if len(sys.argv) < 2:
print('Usage: python src/predict.py <url>')
sys.exit(1)
url = sys.argv[1]
print(predict_single(url))