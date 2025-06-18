import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

st.title("Sentiment Analysis (AI / ML)")

# Load dataset
st.write("Loading dataset...")
try:
    df = pd.read_csv("Dataset/sentiment_reviews_augmented.csv", encoding="latin1", on_bad_lines='skip')
    df.columns = df.columns.str.strip()  # Remove any extra whitespace from column names

    # Rename to expected column names
    df.rename(columns={'Text': 'text', 'Sentiment': 'label'}, inplace=True)

    st.success("Dataset loaded successfully!")
except Exception as e:
    st.error(f"Failed to load dataset: {e}")
    st.stop()

# Show sample data
st.write("Sample Data:")
st.dataframe(df.head())

# Check if required columns exist
if 'text' not in df.columns or 'label' not in df.columns:
    st.error("Dataset must have 'text' and 'label' columns.")
    st.stop()

# Features and labels
X = df["text"]
y = df["label"]

# Split into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('nb', MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Model Accuracy: **{accuracy:.2f}**")

# Save model
model_path = "sentiment_model.pkl"
joblib.dump(model, model_path)
st.success(f"Model saved as {model_path}")

# User input for prediction
st.subheader("Try the model")
user_input = st.text_input("Enter a sentence to analyze sentiment:")
if user_input:
    prediction = model.predict([user_input])[0]
    st.write(f"Predicted Sentiment: **{prediction}**")
