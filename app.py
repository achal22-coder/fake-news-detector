import streamlit as st
import joblib

# Load the trained model and vectorizer
model = joblib.load('model/fake_news_model.pkl')
vectorizer = joblib.load('model/tfidf_vectorizer.pkl')

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Enter a news article and I’ll tell you if it’s **Real** or **Fake**.")

# Text input
user_input = st.text_area("📝 Paste your news article here:", height=200)

# Predict button
if st.button("🚀 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Vectorize and predict
        vect_input = vectorizer.transform([user_input])
        prediction = model.predict(vect_input)[0]

        if prediction == 0:
            st.success("✅ This news is **Real**.")
        else:
            st.error("❌ This news is **Fake**.")
