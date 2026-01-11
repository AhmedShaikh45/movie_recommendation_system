# Movie Recommender System 🎬

A machine learning-based recommendation engine that suggests movies using **Content-Based Filtering**. By analyzing movie metadata such as overviews, genres, cast, and crew, the system identifies and recommends films with the highest textual and thematic similarity.

---

## 🚀 Project Overview
The goal of this project is to build a recommendation system that helps users discover movies similar to their favorites. Unlike Collaborative Filtering (which relies on user ratings), this system uses the attributes of the movie itself to find "neighbors" in a high-dimensional vector space.

### Key Features:
* **Data Integration**: Merges TMDB movie datasets and credits for a holistic view.
* **Feature Extraction**: Isolates critical metadata including `genres`, `keywords`, `cast`, and `crew` (Director).
* **Advanced NLP**: Implements text cleaning, space removal for entity integrity, and Porter Stemming.
* **Vectorization**: Uses Bag of Words (CountVectorizer) to convert text into mathematical vectors.
* **Similarity Scoring**: Employs Cosine Similarity to calculate the distance between 4,806 unique movies.

---

## 🛠️ Technical Architecture

### 1. Data Preprocessing
* **Metadata Cleaning**: Specialized functions convert string-ified JSON lists into Python lists to extract names.
* **Entity Processing**: Spaces are removed from names (e.g., "James Cameron" becomes "JamesCameron") to ensure the vectorizer treats full names as single unique tokens.
* **Tag Creation**: An "overview" is combined with genres, keywords, and cast to create a massive "tags" column for each movie.

### 2. Natural Language Processing (NLP)
* **Lowercasing**: All tags are converted to lowercase to maintain consistency.
* **Stemming**: Using the `nltk` PorterStemmer, words are reduced to their root forms (e.g., "activities" becomes "activ") to improve matching accuracy.

### 3. Machine Learning Model
* **Vectorization**: Text is converted into 5,000-dimensional vectors using `CountVectorizer`, excluding common English stop words.
* **Similarity Matrix**: A similarity matrix is generated where each cell represents the cosine distance between two movies.

---

## 📋 Installation & Requirements

### Prerequisites
* Python 3.12.3
* Jupyter Notebook or VS Code

### Libraries Needed
```bash
pip install pandas numpy scikit-learn nltk
