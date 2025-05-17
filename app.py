import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import difflib
import streamlit as st
from io import StringIO

# Embedded CSV content
csv_data = """title,genres,keywords,cast,director
The Matrix,Action,Sci-fi,Keanu Reeves,Lana Wachowski
Inception,Action,Sci-fi,Leonardo DiCaprio,Christopher Nolan
Interstellar,Adventure,Space,Matthew McConaughey,Christopher Nolan
...
"""  # Replace with your actual data

# Load CSV from string
df_chunk = pd.read_csv(StringIO(csv_data))

# Preprocessing
def clean_data(x):
    return x.lower().strip().replace(" ", "") if isinstance(x, str) else ""

required_features = ["genres", "keywords", "cast", "director", "title"]
for feature in required_features:
    if feature not in df_chunk.columns:
        df_chunk[feature] = ""
    df_chunk[feature] = df_chunk[feature].fillna("").apply(clean_data)

df_chunk["combined_features"] = df_chunk["genres"] + " " + df_chunk["keywords"] + " " + df_chunk["cast"] + " " + df_chunk["director"]

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df_chunk["combined_features"])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Reverse index
df_chunk = df_chunk.reset_index()
indices = pd.Series(df_chunk.index, index=df_chunk["title"].str.lower().str.strip()).drop_duplicates()

def get_closest_match(title):
    possible_matches = df_chunk["title"].str.lower().str.strip().tolist()
    matches = difflib.get_close_matches(title.lower().strip(), possible_matches, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_recommendations(title):
    matched_title = get_closest_match(title)
    if not matched_title:
        return f"'{title}' not found in the dataset."

    idx = indices[matched_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df_chunk["title"].iloc[movie_indices]

# Streamlit UI
st.title("AI Movie Recommender System")
movie_name = st.text_input("Enter a movie title:")

if movie_name:
    recommendations = get_recommendations(movie_name)
    st.subheader("Top 10 Recommendations:")
    if isinstance(recommendations, str):
        st.write(recommendations)
    else:
        for i, title in enumerate(recommendations, 1):
            st.write(f"{i}. {title}")
