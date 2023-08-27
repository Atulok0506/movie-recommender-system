# <span style="color: #FF5733;">Movie Recommender System</span> 
![Programming Language](https://img.shields.io/badge/Python-3.10-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-TMDB-fcba03)
![Deploy](https://img.shields.io/badge/AWS-fcba03)

Welcome to the <span style="color: #FF5733;">Movie Recommender System</span>, your gateway to a personalized movie-watching experience!

## Overview

This end-to-end machine learning model leverages content-based recommendation techniques to bring you the perfect movies for every mood. The system is powered by the TMDB dataset and combines data preprocessing, vectorization, and cosine similarity to deliver tailored movie suggestions.

## How It Works

1. **<span style="color: #FF5733;">Data Processing:</span>** The TMDB dataset is preprocessed and cleaned to extract essential features such as movie titles, descriptions, and genres.

2. **<span style="color: #FF5733;">Text Vectorization:</span>** Movie descriptions undergo text vectorization using TF-IDF (Term Frequency-Inverse Document Frequency) to convert textual content into numerical feature vectors.

3. **<span style="color: #FF5733;">Cosmic Cosine Similarity:</span>** Cosine similarity is employed to measure the similarity between the vectorized descriptions of movies. Movies with similar vector angles are identified, representing those with comparable content and themes.

<div align="center">
  <img src="https://github.com/Atulok0506/movie-recommender-system/blob/main/download%20(3).png" alt="Cosine Similarity Geometry" width="400"/>
</div>

4. **<span style="color: #FF5733;">Recommendation Generation:</span>** Given a user's chosen movie, the system calculates the cosine similarity score between that movie and all others in the dataset. The top-n movies with the highest similarity scores are recommended, ensuring a personalized movie selection.

5. **<span style="color: #FF5733;">Deployment:</span>** The model is deployed using Streamlit, a user-friendly framework for creating interactive web applications. The system is hosted on an AWS EC2 instance, making it accessible through a web browser.

## Key Features

- 🍿 **<span style="color: #FF5733;">Personalized Recommendations:</span>** Discover movies that match your preferences, making every movie night unique.
- 📊 **<span style="color: #FF5733;">Content-Based Approach:</span>** The system analyzes movie content and suggests similar films, capturing the essence of your preferred genres.
- 🧠 **<span style="color: #FF5733;">Cosmic Cosine Similarity:</span>** Unlocks the magic of cosine similarity for movie matchmaking, ensuring accurate and relevant suggestions.
- 🚀 **<span style="color: #FF5733;">Deployed on AWS EC2:</span>** Experience seamless recommendations via the deployed model on [AWS EC2](http://13.235.17.226:8501/).

## Project Structure

- 📄 **<span style="color: #FF5733;">app.py:</span>** The core script to run the recommendation system.
- 📄 **<span style="color: #FF5733;">similarity.pkl:</span>** Contains similarity scores for movies.
- 📄 **<span style="color: #FF5733;">movie_dict.pkl:</span>** Contains movie information.
- 📄 **<span style="color: #FF5733;">movie_recomm.pem:</span>** AWS EC2 PEM file.
## Usage

1. <span style="color: #FF5733;">Clone the repository:</span> `git clone https://github.com/Atulok0506/movie-recommender.git`
2. <span style="color: #FF5733;">Install dependencies:</span> `pip install -r requirements.txt`
3. <span style="color: #FF5733;">Run the model:</span> `streamlit run app.py`

## Contributing

Contributions are welcome! Whether it's enhancing the recommendation algorithms or refining the user interface, your ideas can make this system even better.

## Connect with Me

Got feedback or suggestions? Connect with me on <span style="color: #FF5733;">[LinkedIn](https://www.linkedin.com/in/atul-kishore-b16991179/)</span>.

## Acknowledgments

Special thanks to TMDB for providing the dataset that powers this system.

---

<div align="center">
  <sub>Created by Atul Kishore with 🎬🍿</sub>
</div>

<!-- Theme customization parameters:
title_color: "#FF5733"
text_color: "#434d58"
icon_color: "#4c71f2"
border_color: "#e4e2e2" (Does not apply when hide_border is enabled)
bg_color: "#fffefe" or a gradient in the form of angle,start,end
hide_border: false
theme: "default" or choose from all available themes
cache_seconds: 14400 (4 hours)
locale: "en"
border_radius: 4.5 -->