🎬 Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on user selection. Built using Machine Learning and Streamlit.


![Home](https://github.com/kaushalkumar123456/Movie-Recommender-System/blob/995d6cea66f3875cc54fe89fa4574f5981f9b525/1.png)



![Home](https://github.com/kaushalkumar123456/Movie-Recommender-System/blob/6df4cc34bb28b5a32dcfa8b1c52e3cde16a89e5e/2.png)





📌 Overview

This project recommends movies similar to a selected movie using content-based filtering. It analyzes movie metadata such as genres, cast, crew, and keywords to compute similarity between movies.


✨ Features

🔍 Movie similarity search

🎥 TMDB dataset based recommendations

⚡ Fast cosine similarity engine

🖥️ Interactive Streamlit UI

📊 Machine learning based system




🧠 How It Works

Movie metadata is processed

Important features are combined into tags

Tags converted to vectors using CountVectorizer

Cosine similarity calculated between movies

Top similar movies are recommended





🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Pickle


📂 Project Structure

movie-recommender-system/
│
├── app.py
├── model/
│   ├── movie_list.pkl
│   └── similarity.pkl
├── notebook.ipynb
└── README.md



[Watch Demo](https://github.com/kaushalkumar123456/Movie-Recommender-System/blob/02a1281932213fda5b192bd9b5a6971f3f9b4011/Movie.mp4)




⚙️ Installation
Step 1: Clone repository


git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system


Step 2: Create virtual environment
python -m venv venv

Activate:
Windows
venv\Scripts\activate

Mac/Linux

source venv/bin/activate

pip install streamlit pandas numpy scikit-learn

▶️ How to Run

streamlit run app.py


Then open: http://localhost:8501






