# src\train.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
from features import url_features, extract_tokens

def main():
    df = pd.read_csv('data/raw/urls.csv')

    feats = df['url'].apply(lambda u: pd.Series(url_features(u)))
    tokens = df['url'].apply(lambda u: ' '.join(extract_tokens(u)))

    vectorizer = TfidfVectorizer(max_features=200)
    X_text = vectorizer.fit_transform(tokens)
    X_num = feats.values
    X = hstack([X_num, X_text])
    y = df['label'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=50, random_state=42)
    rf.fit(X_train, y_train)

    acc = rf.score(X_test, y_test)
    print('RF Accuracy:', acc)

    joblib.dump({'model': rf, 'vectorizer': vectorizer}, 'models/rf_model.joblib')
    print('Saved model to models/rf_model.joblib')

if __name__ == '__main__':
    main()
