

# 🎬 AI Movie Recommender System

This is a simple content-based movie recommender system built using **Python**, **scikit-learn**, and **Streamlit**. It suggests similar movies based on input using **TF-IDF** vectorization and **cosine similarity**.

## 🚀 Features

* 🔍 Input a movie title and get top 10 similar movie recommendations.
* ✅ Built-in accuracy testing using predefined movie pairs.
* 📦 Uses an embedded dataset of 20 popular movies.
* 🧠 Intelligent title matching using fuzzy logic (`difflib`).
* 💻 Easy-to-use Streamlit web interface.

## 🧠 How It Works

1. **Data Preparation:** The movie metadata (genres, keywords, cast, director) is cleaned and combined.
2. **Vectorization:** TF-IDF is applied to these features to generate numerical vectors.
3. **Similarity Calculation:** Cosine similarity is computed between all movie pairs.
4. **Recommendation:** For a given title, similar movies are ranked and returned.

## 📋 Sample Dataset

The recommender uses an embedded CSV dataset of 20 movies. Each movie entry includes:

* Title
* Genres
* Keywords
* Cast
* Director

## 📦 Requirements

Install the necessary packages before running the app:

```bash
pip install pandas scikit-learn streamlit
```

## 🛠️ How to Run

To launch the Streamlit app:

```bash
streamlit run app.py
```

Replace `app.py` with the filename containing your code if it's named differently.

## 🖥️ Usage

1. Enter a movie title in the input field.
2. Click **"Get Recommendations"** to see the top 10 similar movies.
3. Optionally, click **"Run Accuracy Test"** to see how well the system performs on known similar movie pairs.

## 🧪 Accuracy Testing

The accuracy test checks whether known similar movies appear in the top 10 results. It runs 5 hardcoded test cases and returns a percentage score.

## 📁 File Structure

```
app.py            # Main application script
README.md         # Project documentation (this file)
```

## 📝 Example Queries

Try typing:

* `Inception`
* `The Lion King`
* `Shutter Island`
* `Iron Man`

## ⚠️ Notes

* The dataset is small and static, designed for demonstration purposes.
* Matching is fuzzy but may still miss titles with significant spelling differences.

## 📖 License

This project is for educational and non-commercial use.

