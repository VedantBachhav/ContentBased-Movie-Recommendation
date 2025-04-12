# import pandas as pd
# import streamlit as st
# import pickle
# import requests


# # ================================
# # ✅ Fetch Poster Function
# # ================================
# def fetch_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c5f7a4ee38cf0607bda0836b76f3ca99"
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()

#         # Check if poster_path is valid
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Use a valid fallback poster if no poster available
#             return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching poster: {e}")
#         # Return fallback image in case of any error
#         return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"


# # ================================
# # ✅ Recommend Function
# # ================================
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]  # Top 10 movies

#     recommended_movies = []
#     recommended_movies_posters = []

#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         # Fetch poster from API
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))

#     return recommended_movies, recommended_movies_posters


# # ================================
# # ✅ Load Movies and Similarity Parts
# # ================================
# movies_dict = pickle.load(open("movies_dict.pkl", 'rb'))
# movies = pd.DataFrame(movies_dict)

# # Load and merge similarity parts
# similarity_parts = []
# for i in range(1, 9):  # Loop through 4 parts
#     with open(f"part_{i}.pkl", "rb") as f:
#         similarity_parts.extend(pickle.load(f))

# # Create the full similarity object
# similarity = similarity_parts

# # ================================
# # 🎬 Streamlit UI
# # ================================
# st.title("🎬 Movie Recommender System")

# # Dropdown to select a movie
# selected_movies_name = st.selectbox(
#     "Select a movie to get recommendations:",
#     movies['title'].values
# )

# # If button is pressed, get recommendations
# if st.button("Recommend"):
#     names, posters = recommend(selected_movies_name)

#     # Create rows dynamically with 5 columns per row
#     num_movies = len(names)
#     num_cols = 5  # 5 columns per row

#     for i in range(0, num_movies, num_cols):
#         cols = st.columns(num_cols)  # Create 5 equal columns dynamically
#         for j in range(num_cols):
#             if i + j < num_movies:
#                 with cols[j]:
#                     st.image(posters[i + j], width=150)  # Set consistent width
#                     st.write(f"**{names[i + j]}**")  # Bold movie names

# import pandas as pd
# import streamlit as st
# import pickle
# import requests
#
#
#
# # def fetch_poster(movie_id):
# #     response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c5f7a4ee38cf0607bda0836b76f3ca99")
# #     data = response.json()
# #     # st.text(data)
# #     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
#
# def fetch_poster(movie_id):
#     try:
#         url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c5f7a4ee38cf0607bda0836b76f3ca99"
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#
#         # Check if poster_path is valid
#         if 'poster_path' in data and data['poster_path']:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         else:
#             # Use a valid fallback poster from a reliable source
#             return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
#
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching poster: {e}")
#         # Return fallback image in case of any error
#         return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
#
#
# # def recommend(movie):
# #     movie_index = movies[movies['title'] == movie].index[0]
# #     distances = similarity[movie_index]
# #     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
# #
# #     recommended_movies = []
# #
# #     recommended_movies_posters = []
# #
# #     for i in movies_list:
# #         movie_id = movies.iloc[i[0]].movie_id
# #         #fetch poster from API
# #         recommended_movies.append(movies.iloc[i[0]].title)
# #         recommended_movies_posters.append(fetch_poster(movie_id))
# #     return recommended_movies, recommended_movies_posters
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]  # Top 10 movies
#
#     recommended_movies = []
#     recommended_movies_posters = []
#
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         # Fetch poster from API
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters
#
#
#
# movies_dict = pickle.load(open("movies_dict.pkl",'rb'))
# movies= pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open("similarity.pkl", 'rb'))
#
# st.title("🎬 Movie Recommender System")
#
# selected_movies_name = st.selectbox(
#     "Select a movie to get recommendations:",
#     movies['title'].values
# )
#
#
#
# # if st.button("Recommend"):
# #     names, posters = recommend(selected_movies_name)
# #
# #     # Create 2 rows of 5 columns each
# #     col1, col2, col3, col4, col5 = st.columns(5)
# #     col6, col7, col8, col9, col10 = st.columns(5)
# #
# #     # Display first 5 movies in row 1
# #     with col1:
# #         st.text(names[0])
# #         st.image(posters[0])
# #     with col2:
# #         st.text(names[1])
# #         st.image(posters[1])
# #     with col3:
# #         st.text(names[2])
# #         st.image(posters[2])
# #     with col4:
# #         st.text(names[3])
# #         st.image(posters[3])
# #     with col5:
# #         st.text(names[4])
# #         st.image(posters[4])
# #
# #     # Display next 5 movies in row 2
# #     with col6:
# #         st.text(names[5])
# #         st.image(posters[5])
# #     with col7:
# #         st.text(names[6])
# #         st.image(posters[6])
# #     with col8:
# #         st.text(names[7])
# #         st.image(posters[7])
# #     with col9:
# #         st.text(names[8])
# #         st.image(posters[8])
# #     with col10:
# #         st.text(names[9])
# #         st.image(posters[9])
#
#
# if st.button("Recommend"):
#     names, posters = recommend(selected_movies_name)
#
#     # Create rows dynamically with 5 columns per row
#     num_movies = len(names)
#     num_cols = 5  # 5 columns per row
#
#     for i in range(0, num_movies, num_cols):
#         cols = st.columns(num_cols)  # Create 5 equal columns dynamically
#         for j in range(num_cols):
#             if i + j < num_movies:
#                 with cols[j]:
#                     st.image(posters[i + j], width=150)  # Set consistent width
#                     st.write(f"**{names[i + j]}**")  # Bold movie names
#
#
#
#
# # Invalid Poster URL:
#
# # The URL provided by the TMDB API might be incorrect or the poster path is None or null.
# # API Rate Limit Exceeded:
# # The TMDB API might have hit the request limit, blocking further requests.
# # Incorrect API Key:
# # Ensure the API key is correct and valid.
# # Network/Firewall Issues:
# # Local firewall or VPN may block the connection.

import streamlit as st
import pickle
import requests
import pandas as pd

# ================================
# ✅ Fetch Poster Function
# ================================
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c5f7a4ee38cf0607bda0836b76f3ca99"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Check if poster_path is valid
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            # Use a valid fallback poster if no poster available
            return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        # Return fallback image in case of any error
        return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"


# ================================
# ✅ Recommend Function
# ================================
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        
        if movie_index >= len(similarity):
            raise IndexError(f"Movie index {movie_index} is out of range for similarity list.")
        
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]  # Top 10 movies

        recommended_movies = []
        recommended_movies_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            # Fetch poster from API
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))

        return recommended_movies, recommended_movies_posters
    except IndexError as e:
        st.error(f"IndexError: {e}")
        return [], []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []


# ================================
# ✅ Load Pickle Parts Function
# ================================
def load_pickle_parts(parts):
    combined_data = []
    for part in parts:
        try:
            with open(part, 'rb') as f:
                data = pickle.load(f, encoding='latin1')
                combined_data.append(data)
        except pickle.UnpicklingError as e:
            print(f"Error loading part {part}: {e}")
        except Exception as e:
            print(f"Error loading part {part}: {e}")
    
    # Combine the data (assuming data is a list or can be concatenated)
    return combined_data


# ================================
# ✅ Load Movies and Similarity Data
# ================================
# List of part files for similarity data
pickle_parts = [
    "part_1.pkl", "part_2.pkl", "part_3.pkl", "part_4.pkl", 
    "part_5.pkl", "part_6.pkl", "part_7.pkl", "part_8.pkl"
]

# Load the pickle parts and combine them
combined_similarity = load_pickle_parts(pickle_parts)

# Assuming the data can be concatenated or merged, adjust based on your structure
# If it's a DataFrame, you can concatenate them
similarity = pd.concat(combined_similarity, ignore_index=True)

# Load the movies_dict.pkl
movies_dict = None
with open("movies_dict.pkl", 'rb') as f:
    movies_dict = pickle.load(f, encoding='latin1')

# Convert movies_dict to DataFrame
movies = pd.DataFrame(movies_dict)

# ================================
# Streamlit App Interface
# ================================
st.title("Movie Recommendation System")

# User input for movie title
movie_title = st.text_input("Enter a movie title", "")

# If the user inputs a movie title, make recommendations
if movie_title:
    recommended_movies, recommended_movies_posters = recommend(movie_title)
    
    if recommended_movies:
        st.write("Recommended Movies:")

        # Display recommended movies and their posters
        for i in range(len(recommended_movies)):
            st.image(recommended_movies_posters[i], width=150)
            st.text(recommended_movies[i])
    else:
        st.write("No recommendations found.")
