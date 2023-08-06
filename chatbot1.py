import os
import json
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter
    st.set_page_config(
        page_title="Chatbot",
        layout="wide",
        initial_sidebar_state="auto",
        page_icon="🤖"
    )
    st.markdown(
        "<div style='text-align: center;'><h1>Chatbot 🤖</h1></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='text-align: center;'><p>Welcome to the chatbot. Please type a message and press Enter.</p></div>",
        unsafe_allow_html=True
    )

    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if user_input:
        # Convert the user input to a string
        user_input_str = str(user_input)

        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=120, max_chars=None, key=f"chatbot_response_{counter}")

        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == '__main__':
    main()
