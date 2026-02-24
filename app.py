# import pickle
# import streamlit as st
# import requests
#
# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#
#     return recommended_movie_names,recommended_movie_posters
#
#
# st.header('Movie Recommender System')
# movies = pickle.load(open('model/movie_list.pkl','rb'))
# similarity = pickle.load(open('model/similarity.pkl','rb'))
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )
#
# if st.button('Show Recommendation'):
#     recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])
#
#
#
#
#


# For Trailer

# import pickle
# import streamlit as st
# import requests
#
# # ------------------ CONFIG ------------------
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
#
# # ------------------ FUNCTIONS ------------------
#
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#
#         poster_path = data.get("poster_path")
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#
#     except requests.exceptions.RequestException:
#         pass
#
#     return None
#
#
# def fetch_trailer(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#
#         for video in data.get("results", []):
#             if video.get("site") == "YouTube" and video.get("type") == "Trailer":
#                 return f"https://www.youtube.com/watch?v={video['key']}"
#
#     except requests.exceptions.RequestException:
#         pass
#
#     return None
#
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(
#         list(enumerate(similarity[index])),
#         reverse=True,
#         key=lambda x: x[1]
#     )
#
#     names, posters, trailers = [], [], []
#
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         names.append(movies.iloc[i[0]].title)
#         posters.append(fetch_poster(movie_id))
#         trailers.append(fetch_trailer(movie_id))
#
#     return names, posters, trailers
#
#
# # ------------------ LOAD DATA ------------------
#
# movies = pickle.load(open('model/movie_list.pkl', 'rb'))
# similarity = pickle.load(open('model/similarity.pkl', 'rb'))
#
# # ------------------ UI ------------------
#
# st.title("🎬 Movie Recommender System")
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )
#
# if st.button("Show Recommendation"):
#     names, posters, trailers = recommend(selected_movie)
#     cols = st.columns(5)
#
#     for i in range(5):
#         with cols[i]:
#             st.text(names[i])
#
#             if posters[i] and trailers[i]:
#                 st.markdown(
#                     f"""
#                     <a href="{trailers[i]}" target="_blank">
#                         <img src="{posters[i]}" style="width:100%; border-radius:10px;">
#                     </a>
#                     """,
#                     unsafe_allow_html=True
#                 )
#             elif posters[i]:
#                 st.image(posters[i])
#             else:
#                 st.write("Poster not available")






# For Movies


#
# import pickle
# import streamlit as st
# import requests
#
# # ------------------ CONFIG ------------------
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
#
# # ------------------ FUNCTIONS ------------------
#
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#
#         poster_path = data.get("poster_path")
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#
#     except requests.exceptions.RequestException:
#         pass
#
#     return None
#
#
# def get_watch_url(movie_name):
#     query = movie_name.replace(" ", "+")
#     return f"https://www.google.com/search?q=watch+{query}+movie"
#
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(
#         list(enumerate(similarity[index])),
#         reverse=True,
#         key=lambda x: x[1]
#     )
#
#     names, posters = [], []
#
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         names.append(movies.iloc[i[0]].title)
#         posters.append(fetch_poster(movie_id))
#
#     return names, posters
#
#
# # ------------------ LOAD DATA ------------------
#
# movies = pickle.load(open('model/movie_list.pkl', 'rb'))
# similarity = pickle.load(open('model/similarity.pkl', 'rb'))
#
# # ------------------ UI ------------------
#
# st.title("🎬 Movie Recommender System")
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )
#
# if st.button("Show Recommendation"):
#     names, posters = recommend(selected_movie)
#     cols = st.columns(5)
#
#     for i in range(5):
#         with cols[i]:
#             st.text(names[i])
#
#             if posters[i]:
#                 st.image(posters[i])
#
#             watch_url = get_watch_url(names[i])
#
#             st.markdown(
#                 f"""
#                 <a href="{watch_url}" target="_blank">
#                     <button style="
#                         width:100%;
#                         padding:8px;
#                         background-color:#e50914;
#                         color:white;
#                         border:none;
#                         border-radius:6px;
#                         cursor:pointer;">
#                         🎬 Watch Full Movie
#                     </button>
#                 </a>
#                 """,
#                 unsafe_allow_html=True
#             )








# For Final



#
# import pickle
# import streamlit as st
# import requests
#
# # ------------------ CONFIG ------------------
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
#
# # ------------------ FUNCTIONS ------------------
#
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         poster_path = data.get("poster_path")
#         if poster_path:
#             return "https://image.tmdb.org/t/p/w500/" + poster_path
#     except requests.exceptions.RequestException:
#         pass
#     return None
#
#
# def fetch_trailer(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US"
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         for video in data.get("results", []):
#             if video.get("site") == "YouTube" and video.get("type") == "Trailer":
#                 return f"https://www.youtube.com/watch?v={video['key']}"
#     except requests.exceptions.RequestException:
#         pass
#     return None
#
#
# def get_watch_url(movie_name):
#     query = movie_name.replace(" ", "+")
#     return f"https://www.google.com/search?q=watch+{query}+movie"
#
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(
#         list(enumerate(similarity[index])),
#         reverse=True,
#         key=lambda x: x[1]
#     )
#
#     recommendations = []
#
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommendations.append({
#             "title": movies.iloc[i[0]].title,
#             "poster": fetch_poster(movie_id),
#             "trailer": fetch_trailer(movie_id),
#             "watch_url": get_watch_url(movies.iloc[i[0]].title)
#         })
#
#     return recommendations
#
#
# # ------------------ LOAD DATA ------------------
#
# movies = pickle.load(open('model/movie_list.pkl', 'rb'))
# similarity = pickle.load(open('model/similarity.pkl', 'rb'))
#
# # ------------------ UI ------------------
#
# st.title("🎬 Movie Recommender System")
#
# movie_list = movies['title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie",
#     movie_list
# )
#
# if st.button("Show Recommendation"):
#     recommendations = recommend(selected_movie)
#     cols = st.columns(5)
#
#     for col, movie in zip(cols, recommendations):
#         with col:
#             st.subheader(movie["title"])
#
#             if movie["poster"]:
#                 st.image(movie["poster"], use_column_width=True)
#
#             # 🎞 Trailer first
#             if movie["trailer"]:
#                 st.markdown(f"[▶ Watch Trailer]({movie['trailer']})")
#             else:
#                 st.caption("Trailer not available")
#
#             # 🎬 Full movie link
#             st.markdown(
#                 f"""
#                 <a href="{movie['watch_url']}" target="_blank">
#                     <button style="
#                         width:100%;
#                         padding:8px;
#                         margin-top:6px;
#                         background-color:#e50914;
#                         color:white;
#                         border:none;
#                         border-radius:6px;
#                         cursor:pointer;">
#                         🎬 Watch Full Movie
#                     </button>
#                 </a>
#                 """,
#                 unsafe_allow_html=True
#             )








#
# import pickle
# import streamlit as st
# import requests
#
# # ------------------ CONFIG ------------------
# st.set_page_config(page_title="Movie Recommender", layout="wide")
#
# API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
#
# # ------------------ FUNCTIONS ------------------
#
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     try:
#         r = requests.get(url, timeout=5)
#         r.raise_for_status()
#         data = r.json()
#         if data.get("poster_path"):
#             return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
#     except requests.exceptions.RequestException:
#         pass
#     return None
#
#
# def fetch_trailer(movie_id):
#     """
#     Returns YouTube Trailer OR Teaser if Trailer is not available
#     """
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={c287b29a58ce875deb8123056f1b5d5d}&language=en-US"
#     try:
#         r = requests.get(url, timeout=5)
#         r.raise_for_status()
#         data = r.json()
#
#         # Priority: Trailer > Teaser
#         for video in data.get("results", []):
#             if video.get("site") == "YouTube" and video.get("type") == "Trailer":
#                 return f"https://www.youtube.com/watch?v={video['key']}"
#
#         for video in data.get("results", []):
#             if video.get("site") == "YouTube" and video.get("type") == "Teaser":
#                 return f"https://www.youtube.com/watch?v={video['key']}"
#
#     except requests.exceptions.RequestException:
#         pass
#
#     return None
#
#
# def get_watch_url(movie_name):
#     query = movie_name.replace(" ", "+")
#     return f"https://www.google.com/search?q=watch+{query}+movie"
#
#
# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(
#         enumerate(similarity[index]),
#         key=lambda x: x[1],
#         reverse=True
#     )
#
#     recs = []
#
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         title = movies.iloc[i[0]].title
#
#         recs.append({
#             "title": title,
#             "poster": fetch_poster(movie_id),
#             "trailer": fetch_trailer(movie_id),
#             "watch": get_watch_url(title)
#         })
#
#     return recs
#
#
# # ------------------ LOAD DATA ------------------
#
# movies = pickle.load(open("model/movie_list.pkl", "rb"))
# similarity = pickle.load(open("model/similarity.pkl", "rb"))
#
# # ------------------ UI ------------------
#
# st.title("🎬 Movie Recommender System")
#
# selected_movie = st.selectbox(
#     "Type or select a movie",
#     movies["title"].values
# )
#
# if st.button("Show Recommendation"):
#     recommendations = recommend(selected_movie)
#     cols = st.columns(5)
#
#     for col, movie in zip(cols, recommendations):
#         with col:
#             st.subheader(movie["title"])
#
#             if movie["poster"]:
#                 st.image(movie["poster"], use_column_width=True)
#
#             # 🎞 Show trailer ONLY if available
#             if movie["trailer"]:
#                 st.markdown(f"[▶ Watch Trailer]({movie['trailer']})")
#
#             # 🎬 Full movie redirect (always shown)
#             st.markdown(
#                 f"""
#                 <a href="{movie['watch']}" target="_blank">
#                     <button style="
#                         width:100%;
#                         padding:8px;
#                         margin-top:6px;
#                         background-color:#e50914;
#                         color:white;
#                         border:none;
#                         border-radius:6px;
#                         cursor:pointer;">
#                         🎬 Watch Full Movie
#                     </button>
#                 </a>
#                 """,
#                 unsafe_allow_html=True
#             )




import pickle
import streamlit as st
import requests

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# ✅ API KEY MUST BE A STRING
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# ------------------ FUNCTIONS ------------------

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    except requests.exceptions.RequestException:
        pass
    return None


def fetch_trailer(movie_id):
    """
    Returns YouTube Trailer or Teaser (fallback)
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()

        # Priority 1: Trailer
        for video in data.get("results", []):
            if video.get("site") == "YouTube" and video.get("type") == "Trailer":
                return f"https://www.youtube.com/watch?v={video['key']}"

        # Priority 2: Teaser
        for video in data.get("results", []):
            if video.get("site") == "YouTube" and video.get("type") == "Teaser":
                return f"https://www.youtube.com/watch?v={video['key']}"

    except requests.exceptions.RequestException:
        pass

    return None


def get_watch_url(movie_name):
    query = movie_name.replace(" ", "+")
    return f"https://www.google.com/search?q=watch+{query}+movie"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        enumerate(similarity[index]),
        key=lambda x: x[1],
        reverse=True
    )

    recs = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title

        recs.append({
            "title": title,
            "poster": fetch_poster(movie_id),
            "trailer": fetch_trailer(movie_id),
            "watch": get_watch_url(title)
        })

    return recs


# ------------------ LOAD DATA ------------------

movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

# ------------------ UI ------------------

st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Type or select a movie",
    movies["title"].values
)
#
# if st.button("Show Recommendation"):
#     recommendations = recommend(selected_movie)
#     cols = st.columns(5)
#
#     for col, movie in zip(cols, recommendations):
#         with col:
#             st.subheader(movie["title"])
#
#             if movie["poster"]:
#                 st.image(movie["poster"], use_column_width=True)
#
#             # 🎞 Trailer (only if available)
#             if movie["trailer"]:
#                 st.markdown(f"[▶ Watch Trailer]({movie['trailer']})")
#
#             # 🎬 Full movie redirect
#             st.markdown(
#                 f"""
#                 <a href="{movie['watch']}" target="_blank">
#                     <button style="
#                         width:100%;
#                         padding:8px;
#                         margin-top:6px;
#                         background-color:#e50914;
#                         color:white;
#                         border:none;
#                         border-radius:6px;
#                         cursor:pointer;">
#                         🎬 Watch Full Movie
#                     </button>
#                 </a>
#                 """,
#                 unsafe_allow_html=True
#             )





if st.button("Show Recommendation"):
    recommendations = recommend(selected_movie)
    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):
        with col:
            st.subheader(movie["title"])

            # 🎬 Clickable Poster (Trailer)
            if movie["poster"] and movie["trailer"]:
                st.markdown(
                    f"""
                    <a href="{movie['trailer']}" target="_blank">
                        <img src="{movie['poster']}" style="
                            width:100%;
                            border-radius:12px;
                            box-shadow:0 6px 20px rgba(0,0,0,0.6);
                        ">
                    </a>
                    """,
                    unsafe_allow_html=True
                )
            elif movie["poster"]:
                st.image(movie["poster"], use_column_width=True)

            # ▶ Watch Trailer Button
            if movie["trailer"]:
                st.markdown(
                    f"""
                    <a href="{movie['trailer']}" target="_blank" style="text-decoration:none;">
                        <button style="
                            width:100%;
                            padding:7px;
                            margin-top:8px;
                            background: linear-gradient(90deg, #1f80e0, #4facfe);
                            color:white;
                            font-size:14px;
                            font-weight:600;
                            border:none;
                            border-radius:8px;
                            cursor:pointer;">
                            ▶ Watch Trailer
                        </button>
                    </a>
                    """,
                    unsafe_allow_html=True
                )

            # 🎬 Watch Full Movie Button
            st.markdown(
                f"""
                <a href="{movie['watch']}" target="_blank">
                    <button style="
                        width:100%;
                        padding:8px;
                        margin-top:6px;
                        background-color:#e50914;
                        color:white;
                        border:none;
                        border-radius:8px;
                        font-weight:600;
                        cursor:pointer;">
                        🎬 Watch Full Movie
                    </button>
                </a>
                """,
                unsafe_allow_html=True
            )
