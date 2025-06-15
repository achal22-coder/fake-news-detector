# fake-news-detector
A machine learning project that uses **Natural Language Processing (NLP)** and **Logistic Regression** to classify news articles as **real or fake**. Built as part of my AI learning journey to strengthen NLP and model deployment skills.
# 📰 Fake News Detector 🧠

A machine learning-powered app that detects whether a news article is **Real** or **Fake** based on its content.  
Built using `Python`, `Scikit-learn`, and deployed with `Streamlit`.

> ✅ First project in the Data Science & GenAI Bootcamp  
> 🚀 Built by a BSc CS student choosing industry skills over traditional college  
> 🛠️ Focused on real-world impact, clean code, and deployment

---

## 🔍 Problem Statement

In an age of misinformation, detecting fake news is more important than ever.  
This project uses **Natural Language Processing (NLP)** and **Logistic Regression** to classify news articles.

---

## 💻 Technologies Used

- 🐍 Python 3
- 🧠 Scikit-learn (TF-IDF, Logistic Regression)
- 🧼 NLP: Text cleaning, stopwords, vectorization
- 📊 Pandas, NumPy
- 🌐 [Streamlit](https://streamlit.io) for the web app
- 🗂️ Joblib for model saving

---

## 🚀 Live Demo

🎯 Try it here:  
👉 [Fake News Detector – Streamlit App](https://fake-news-detector-ywtvv2egbac4jbf7szoftc.streamlit.app/)

Paste any news article and get an instant prediction!

---

## 📁 Project Structure

fake-news-detector/
│
├── app.py # Streamlit app file
├── fake-news-detector.ipynb # Main Jupyter notebook
├── model/
│ ├── model.pkl # Trained logistic regression model
│ └── vectorizer.pkl # TF-IDF vectorizer
├── data/
│ ├── true.csv # Real news dataset
│ └── false.csv # Fake news dataset
├── requirements.txt # Python dependencies
└── README.md


---

## 🧠 How It Works

1. **Preprocess** the text: lowercase, remove punctuation, stopwords, etc.
2. **Vectorize** using TF-IDF
3. **Train** logistic regression on labeled data
4. **Save model + vectorizer** using `joblib`
5. **Deploy** using Streamlit for real-time predictions

---

## 🧪 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/achal22-coder/fake-news-detector.git
cd fake-news-detector

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

## 👤 About Me

I'm a BSc Computer Science student who chose to leave traditional college to pursue **industry-relevant, meaningful learning**.  
This is my first project from the **Data Science & GenAI Bootcamp**, where I'm building my portfolio one real-world app at a time.

---


## ⭐ Show Your Support!

If you found this project useful:

- Leave a ⭐ on the repo  
- Connect with me on [LinkedIn](www.linkedin.com/in/achal-shrivas-7b9a08305)  
- Try the app and send feedback!
