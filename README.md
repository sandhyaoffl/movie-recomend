# 🎬 AI Movie Recommendation System

This project is a content-based movie recommendation system built using Python, pandas, and scikit-learn. It analyzes movie metadata to suggest similar movies based on genres, keywords, cast, and director information.

---

## 📂 Dataset

The system utilizes a CSV file named `movies.csv`, which should contain the following columns:

* `title`
* `genres`
* `keywords`
* `cast`
* `director`

Ensure that the dataset is placed in the same directory as the script or provide the correct path to the file.

---

## ⚙️ Features

* **Content-Based Filtering**: Recommends movies by analyzing textual metadata.
* **TF-IDF Vectorization**: Converts textual data into numerical features using Term Frequency-Inverse Document Frequency.
* **Cosine Similarity**: Measures the similarity between movies based on their feature vectors.
* **Fuzzy Title Matching**: Handles user input errors by finding the closest matching movie title.

---

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ai-movie-recommender.git
   cd ai-movie-recommender
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.x installed. Then, install the required Python packages:

   ```bash
   pip install pandas scikit-learn
   ```

---

## 🚀 Usage

1. **Prepare the Dataset**:

   Ensure that `movies.csv` is present in the project directory and contains the necessary columns.

2. **Run the Script**:

   Execute the Python script:

   ```bash
   python movie_recommender.py
   ```

3. **Interact with the System**:

   When prompted, enter a movie title to receive top 10 similar movie recommendations.

---

## 🧠 How It Works

1. **Data Loading**:

   Loads a subset of the dataset (default 1000 rows) to manage memory usage.

2. **Data Preprocessing**:

   * Cleans and standardizes textual data by converting to lowercase and removing spaces.
   * Combines `genres`, `keywords`, `cast`, and `director` into a single string for each movie.

3. **Feature Extraction**:

   Applies TF-IDF vectorization to the combined features to convert text into numerical vectors.

4. **Similarity Computation**:

   Calculates cosine similarity between all movie vectors to determine their closeness.

5. **Recommendation Generation**:

   * Matches user input to the closest movie title using fuzzy matching.
   * Retrieves and displays the top 10 movies with the highest similarity scores.

---

## 📝 Example

```bash
AI Movie Recommender System
Enter a movie title: Inception

Top 10 Recommendations:

1. Interstellar
2. The Prestige
3. Memento
4. The Matrix
5. Shutter Island
6. The Dark Knight
7. The Illusionist
8. Source Code
9. Looper
10. Edge of Tomorrow
```

---

## 📌 Notes

* The default `chunk_size` is set to 1000 to manage memory usage. Adjust this value based on your system's capabilities.
* Ensure that all required columns are present in the dataset. Missing columns are filled with empty strings during preprocessing.
* The fuzzy matching cutoff is set to 0.6. Adjust this threshold in the `get_closest_match` function if needed.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

