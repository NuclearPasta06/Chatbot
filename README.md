# Streamlit Chatbot

The primary objective of this project is to develop an interactive chatbot capable of comprehending and providing appropriate responses based on user input intents. The chatbot's functionality relies on Natural Language Processing (NLP) techniques and the Logistic Regression algorithm to identify intents and entities from the user's input. The entire chatbot is built using Streamlit, a Python library dedicated to creating dynamic web applications.

## Project Overview
The project encompasses two main components:
1. **Training the Chatbot:** Utilizing NLP techniques and the Logistic Regression algorithm to train the chatbot on annotated intents and entities data.
2. **Creating the Chatbot Interface:** Employing the Streamlit web framework to construct a user-friendly, web-based chatbot interface. Users can conveniently input text and instantly receive responses from the chatbot.

## Dataset
The dataset employed in this project consists of labelled intents and entities organized as a list. Each entry contains:
- Intents: Representing the intention behind user input (e.g., "greeting," "budget," "about").
- Entities: Extracted information from user input (e.g., "Hi," "How do I create a budget?", "What is your purpose?")
- Text: The actual user input text.

## Streamlit Chatbot Interface
The heart of this project lies in the Streamlit-powered chatbot interface. The user interface comprises a text input box where users can input their text, and a chat window displays the chatbot's responses. The trained model enables the chatbot to generate appropriate replies based on user input and detected intents.

## Conclusion
In conclusion, this project successfully developed a chatbot with intents-based understanding and response capabilities. By incorporating NLP and Logistic Regression, and integrating Streamlit for the interface, the chatbot provides a seamless user experience. The project could be extended further by augmenting the data, adopting more advanced NLP techniques, or exploring deep learning algorithms to enhance the chatbot's performance.
