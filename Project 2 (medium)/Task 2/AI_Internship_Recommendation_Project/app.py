import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv("internship_data.csv")

# Streamlit UI
st.title("🎓 Internship Domain Recommendation Engine")
st.write("Enter your skills, interests, or experiences to get recommended internship domains.")

# User input
user_input = st.text_input("🔍 Your Skills & Interests (comma-separated):")

if user_input:
    # Preprocessing
    vectorizer = CountVectorizer()
    skill_matrix = vectorizer.fit_transform(df['skills'].tolist() + [user_input])

    # Calculate similarity
    similarity_scores = cosine_similarity(skill_matrix[-1], skill_matrix[:-1])
    top_index = similarity_scores.argsort()[0][::-1]
    recommended_domains = df.loc[top_index[:3], 'domain'].tolist()

    # Display results
    st.subheader("🔥 Recommended Internship Domains for You:")
    for i, domain in enumerate(recommended_domains, 1):
        st.write(f"{i}. {domain}")
