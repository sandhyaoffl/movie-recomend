import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import difflib
import streamlit as st

# Load the dataset with error handling
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("movies1.csv", nrows=1000)
        return df
    except FileNotFoundError:
        st.error("The file 'movies1.csv' was not found. Please upload it.")
        return None

# Basic preprocessing
def clean_data(x):
    return x.lower().strip().replace(" ", "") if isinstance(x, str) else ""

def preprocess(df):
    required_features = ["genres", "keywords", "cast", "director", "title"]
    for feature in required_features:
        if feature not in df.columns:
            df[feature] = ""
        df[feature] = df[feature].fillna("").apply(clean_data)
    df["combined_features"] = (
        df["genres"] + " " + df["keywords"] + " " + df["cast"] + " " + df["director"]
    )
    return df

# Recommendation system
def build_recommender(df):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["combined_features"])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    df = df.reset_index()
    indices = pd.Series(df.index, index=df["title"].str.lower().str.strip()).drop_duplicates()
    return cosine_sim, indices

def get_closest_match(title, titles_list):
    matches = difflib.get_close_matches(title.lower().strip(), titles_list, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_recommendations(title, df, cosine_sim, indices):
    matched_title = get_closest_match(title, df["title"].str.lower().str.strip().tolist())
    if not matched_title:
        return None, f"'{title}' not found in the dataset."
    idx = indices[matched_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df["title"].iloc[movie_indices], None

# Streamlit UI
def main():
    st.title("AI Movie Recommender System")

    df = load_data()
    if df is None:
        return

    df = preprocess(df)
    cosine_sim, indices = build_recommender(df)

    movie_title = st.text_input("Enter a movie title:")
    if st.button("Recommend"):
        if movie_title.strip() == "":
            st.warning("Please enter a movie title.")
        else:
            recommendations, error = get_recommendations(movie_title, df, cosine_sim, indices)
            if error:
                st.error(error)
            else:
                st.subheader("Top 10 Recommendations:")
                for i, title in enumerate(recommendations, 1):
                    st.write(f"{i}. {title}")

if __name__ == "__main__":
    main()
