# There is a file called transformed_data with the following columns
# Date,Time Start,Time End,Tracks,Session Title,Room/Location,Description,Speakers,Role: Moderators,Authors,Recorded Video URL,Session or Sub-session,Tags

import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("transformed_data.csv")

# Create the Streamlit app
st.title("Poster Search by Name")

# Create a search box
search_term = st.text_input("Enter a name to search for:")

if search_term:
    # Filter the data based on the search term
    filtered_data = data[
        data["Session Title"].str.contains(search_term, case=False, na=False)
    ]

    if not filtered_data.empty:
        for _, row in filtered_data.iterrows():
            st.write(f"Poster: {row['Session Title']}")
            st.write(f"Date: {row['Date']}")
            st.write(f"Authors: {row['Authors']}")
            st.write("---")
    else:
        st.write("No matching posters found.")
