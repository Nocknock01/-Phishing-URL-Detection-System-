# src/train.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, accuracy_score
import joblib
from features import url_features, extract_tokens




def featurize_df(df: pd.DataFrame):
# df must have columns: 'url' and 'label' (1=phish, 0=legit)
# handcrafted features
feats = df['url'].apply(url_features).apply(pd.Series)


# token-based features — join tokens for vectorizer
token_series = df['url'].apply(lambda u: ' '.join(extract_tokens(u)))


return feats, token_series




if __name__ == '__main__':
# Load CSV: expected columns url,label
df = pd.read_csv('data/raw/urls.csv')
feats, tokens = featurize_df(df)


# train/test split
X_num = feats.values
vectorizer = TfidfVectorizer(max_features=2000)
X_text = vectorizer.fit_transform(tokens)


from scipy.sparse import hstack
X = hstack([X_num, X_text])
y = df['label'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Random Forest
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
preds = rf.predict(X_test)
print('RF Accuracy:', accuracy_score(y_test, preds))
print(classification_report(y_test, preds))


# Save model and vectorizer
joblib.dump({'model': rf, 'vectorizer': vectorizer}, 'models/rf_model.joblib')


# Optionally train SVM similarly or compare with cross_val_score