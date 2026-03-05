# TED Talks Recommendation System 📺

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)

A content-based recommendation system that suggests TED Talks similar to a selected talk using natural language processing techniques.

## Overview

This project analyzes TED talk descriptions and transcripts to recommend related talks.  
The system converts text data into numerical vectors using TF-IDF and measures similarity using cosine similarity.
Users can interact with the system through a Streamlit web interface to discover new TED Talks based on their interests.

## Features

- Content-based recommendation system
- Text processing using TF-IDF
- Similarity calculation using cosine similarity
- Interactive Streamlit web interface
- Displays recommended TED talks instantly

## 🛠 Technologies Used

| Technology | Purpose |
|-------------|--------|
| Python | Programming language |
| Pandas | Data processing |
| NumPy | Numerical computation |
| Scikit-learn | Machine learning algorithms |
| TF-IDF | Text vectorization |
| Cosine Similarity | Similarity calculation |
| Streamlit | Web interface |

## Project Structure

ted-talk-recommendation
│
├── TED_Talk.csv
├── mainfile.ipynb
├── app.py
├── ted_data.pkl
├── similarity.pkl
├── indices.pkl
└── README.md


## ⚙️ How It Works

1️⃣ Load TED Talks dataset

2️⃣ Combine **description + transcript** to represent talk content

3️⃣ Convert text data into **TF-IDF vectors**

4️⃣ Compute **Cosine Similarity** between talks

5️⃣ Recommend **Top 5 similar TED Talks**

![User Interface Screenshot](User_Interface.png)

## Installation

Clone the repository
``` git clone https://github.com/HasiniPadakandla/TED-Talk-Recommendation-System ```

``` cd TED-Talk-Recommendation-System ```

Install the dependencies

``` pip install pandas scikit-learn streamlit numpy ```

## Run the application

``` streamlit run app.py ```

Then open the browser at:

http://localhost:8501

## Example

Select a TED talk from the dropdown and the system will recommend similar talks based on content similarity.

## Future Improvements

- Hybrid recommendation system
- Deep learning embeddings
- TED video previews
- Improved UI
