import streamlit as st
import pickle
import pandas as pd

# Load saved files
data = pickle.load(open("ted_data.pkl","rb"))
cosine_sim = pickle.load(open("similarity.pkl","rb"))
indices = pickle.load(open("indices.pkl","rb"))

# Recommendation function
def recommend(title):

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    talk_indices = [i[0] for i in sim_scores]

    return data['talk__name'].iloc[talk_indices]


# Streamlit UI
st.title("🎤 TED Talks Recommendation System")

st.write("Select a TED Talk and get similar talk recommendations")

talk_list = data['talk__name'].values

selected_talk = st.selectbox(
    "Choose a TED Talk",
    talk_list
)

if st.button("Recommend"):

    recommendations = recommend(selected_talk)

    st.subheader("Recommended Talks")

    for talk in recommendations:
        st.write("•", talk)