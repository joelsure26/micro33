import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load internship domains data
df = pd.read_csv("internship_data.csv")

# Example user input: skills + interests + experience
user_input = "python pandas machine learning deep learning keras"

# Vectorize both dataset and user input
vectorizer = CountVectorizer()
skill_matrix = vectorizer.fit_transform(df['skills'].tolist() + [user_input])

# Calculate similarity between user input and all domains
similarity_scores = cosine_similarity(skill_matrix[-1], skill_matrix[:-1])

# Recommend top 3 domains
top_index = similarity_scores.argsort()[0][::-1]
recommended_domains = df.loc[top_index[:3], 'domain'].tolist()

# Output result
print("🔥 Recommended Internship Domains for You:")
for i, domain in enumerate(recommended_domains, 1):
    print(f"{i}. {domain}")
