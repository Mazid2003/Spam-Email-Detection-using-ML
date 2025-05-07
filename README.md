# 📧 Spam Email Detection using Machine Learning

This is a web-based application that classifies emails as **Spam** or **Not Spam(Ham)** using **Natural Language Processing (NLP)** and **Machine Learning**. The project includes a Flask-powered interface for real-time predictions.

---

## 🔍 Project Overview

The main goal of this project is to help detect unwanted or malicious emails (spam) using an ML model trained on labeled data. Users can input an email message into the web interface, and the system will predict whether it's spam.

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas & NumPy**
- **NLTK**
- **HTML/CSS** (Flask Templates)

---

## 🧠 Machine Learning Workflow

1. **Data Preprocessing**
   - Lowercasing
   - Removal of punctuation, stopwords
   - Stemming using NLTK

2. **Feature Engineering**
   - Text Vectorization using **TF-IDF**

3. **Model Training**
   - Trained models like:
     - Naive Bayes (best performing)
     - Logistic Regression
     - SVM
   - Evaluated using:
     - Accuracy
     - Precision
     - Recall
     - F1-Score

4. **Deployment**
   - Best model saved using `pickle`
   - Integrated into Flask application

---

## 🌐 Web Application Features

- Input email content via a form
- Click to get prediction: `Spam` or `Not Spam`
- Built using Flask and rendered with Jinja2 templating

---

## 📁 Folder Structure
```
spam-email-detector/
│
├── static/ # CSS styles
├── templates/ # HTML templates
│ ├── home.html
│ └── result.html
├── model/ # Trained ML model (model.pkl)
├── spam_detector.py # ML logic and preprocessing
├── app.py # Flask backend
├── requirements.txt
└── README.md
```
---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Mazid2003/Spam-Email-Detection-using-Machine-Learning.git
cd spam-email-detector
2. Install dependencies

pip install -r requirements.txt
3. Run the Flask App

python app.py
Then open your browser and go to http://localhost:5000

📊 Results
Achieved over 97% accuracy using Multinomial Naive Bayes

Clean preprocessing pipeline

Real-time predictions on the web

✨ Author
Created by Mohammad Mazid
Email:mazidmd750@gmail.com
Linkedin: https://www.linkedin.com/in/mohammadmazid

📜 License
This project is open-source and available under the MIT License.


