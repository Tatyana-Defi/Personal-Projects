
import streamlit as st
import pandas as pd

# load dataset
file_path = "/Users/tatyanadorcinvil/Downloads/movies.csv"
movies_df = pd.read_csv(file_path)

movies_df['Audience score %'] = movies_df['Audience score %'].astype(float)

def recommend_movies_by_genre(genre, min_score,df,top_n=5):
    """
    Recommends movies based on a specified genre and minimum audience score.

    Parameters:
    genre (str): The genre to filter by.
    min_score (float): The minimum audience score percentage.
    df (DataFrame): The dataset containing movie information.
    top_n (int): The number of recommendations to return.

    Returns:
    DataFrame: Recommended movies with their genres and audience scores.
    """
    # Filter movies by genre and audience score
    recommended = df[(df['Genre'].str.contains(genre, case=False)) & 
                     (df['Audience score %'] >= min_score)]
    return recommended[['Film', 'Genre', 'Audience score %']].sort_values(
        by='Audience score %', ascending=False).head(top_n)

#Streamlit App
st.title("Movie Recommendation System")
st.write("Get Movie Recommendation based off of genre and audience score!")



# Example recommendation
genre = st.text_input("Enter a genre (e.g., Comedy, Romance):")
min_score = st.slider("Minimum Audience Score:", 0, 100, 50)
top_n = st.slider("Number of Recommendations:", 1, 10, 5)

if st.button("Get Recommendations"):
    if genre:
        recommendations = recommend_movies_by_genre(genre, min_score, movies_df, top_n)
        if not recommendations.empty:
            st.write("Here are your recommendations:")
            st.dataframe(recommendations)
        else:
            st.write(f"No movies found for genre '{genre}' with a score above {min_score}.")
    else:
        st.write("Please enter a genre.")

