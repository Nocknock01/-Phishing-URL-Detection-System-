🛡️ Phishing URL Detection System (Machine Learning)
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

✨ Features

✅ Detects phishing URLs with high accuracy
✅ Extracts custom URL features (length, digits, special chars, keywords…)
✅ Uses TF-IDF + Random Forest Classifier
✅ Provides real-time prediction API using Flask
✅ Easy to run locally
✅ Clean & extendable project structure

📁 Project Structure

📦 Phishing-URL-Detection-System
├── src/
│   ├── features.py      # Feature extraction logic
│   ├── train.py         # ML training script
│   ├── api.py           # Flask API for prediction
│
├── data/
│   └── raw/urls.csv     # (Your dataset)
│
├── models/
│   └── rf_model.joblib  # Trained ML model
│
├── requirements.txt
└── README.md


⚙️ Installation & Setup

1️⃣ Clone the repo
git clone https://github.com/Nocknock01/-Phishing-URL-Detection-System-.git
cd Phishing-URL-Detection-System

2️⃣ Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add dataset
The dataset should look like

url,label
http://example.com,0
http://malicious.xyz/login,1

Place it in:

data/raw/urls.csv 


🤖 Train the Model::

bash
python src/train.py

Output Example::
 RF Accuracy: 0.91
 Saved model to models/rf_model.jobli
                 
🌐 Run the API Server

bash
python src/api.py

Server starts at::

 cpp
http://127.0.0.1:5000


  📡 Make a Prediction
  PowerShell:
Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post `
  -ContentType "application/json" `
  -Body (ConvertTo-Json @{ url = 'http://example.com/login' })

Example Output:
{
  "url": "http://example.com/login",
  "phishing": false,
  "probability": 0.12
}

🎯 How It Works (Short Summary)

1️⃣ URL features are extracted (length, symbols, keywords, IP, etc.)
2️⃣ TF-IDF converts URL tokens into vector form
3️⃣ Both features are combined
4️⃣ Random Forest model predicts phishing probability
5️⃣ Flask API returns results instantly

Simple → Fast → Accurate 🔥

🧱 Future Improvements

✨ Add deep learning model (LSTM / BERT)
✨ Build a web UI dashboard
✨ Deploy the model using Docker / Render / AWS
✨ Add blacklist + heuristic rules

💬 Author

👤 Srujan M.V
🎓 Cyber Security & Forensics Student
  
★★★★★
