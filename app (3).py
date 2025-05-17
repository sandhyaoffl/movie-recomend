
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import difflib
import streamlit as st

# Load a manageable subset of the dataset
@st.cache_data
def load_data():
    chunk_size = 1000
    df_chunk = pd.read_csv("movies1.csv", nrows=chunk_size)

    def clean_data(x):
        return x.lower().strip().replace(" ", "") if isinstance(x, str) else ""

    required_features = ["genres", "keywords", "cast", "director", "title"]
    for feature in required_features:
        if feature not in df_chunk.columns:
            df_chunk[feature] = ""
        df_chunk[feature] = df_chunk[feature].fillna("").apply(clean_data)

    df_chunk["combined_features"] = (
        df_chunk["genres"] + " "
        + df_chunk["keywords"] + " "
        + df_chunk["cast"] + " "
        + df_chunk["director"]
    )

    return df_chunk

# Build TF-IDF model
@st.cache_resource
def build_model(df_chunk):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df_chunk["combined_features"])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return tfidf, cosine_sim

# Closest title match
def get_closest_match(title, titles_list):
    matches = difflib.get_close_matches(title.lower().strip(), titles_list, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get recommendations
def get_recommendations(title, df_chunk, cosine_sim):
    titles = df_chunk["title"].str.lower().str.strip().tolist()
    matched_title = get_closest_match(title, titles)

    if not matched_title:
        return None, f"No match found for '{title}'. Please try another title."

    indices = pd.Series(df_chunk.index, index=df_chunk["title"].str.lower().str.strip()).drop_duplicates()
    idx = indices[matched_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]

    return df_chunk["title"].iloc[movie_indices].tolist(), None

# Streamlit App
def main():
    st.title("AI Movie Recommender System")

    df_chunk = load_data()
    _, cosine_sim = build_model(df_chunk)

    user_input = st.text_input("Enter a movie title to get recommendations:")

    if user_input:
        recommendations, error = get_recommendations(user_input, df_chunk, cosine_sim)
        if error:
            st.warning(error)
        else:
            st.subheader("Top 10 Recommended Movies:")
            for i, title in enumerate(recommendations, 1):
                st.write(f"{i}. {title}")

if __name__ == "__main__":
    main()
