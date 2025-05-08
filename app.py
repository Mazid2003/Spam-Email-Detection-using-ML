from flask import Flask, request, render_template
import joblib
import re, string

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("spam_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        message = request.form['message']
        cleaned = clean_text(message)
        vect = vectorizer.transform([cleaned])
        prediction = model.predict(vect)[0]
        result = 'Spam' if prediction else 'Ham'
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
