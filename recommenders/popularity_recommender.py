from recommenders import data_movies, data_ratings, default_poster_url
import pandas as pd


def recommend_popular_movies():

    ######################################################################################################
    movie_ratings = pd.merge(data_movies, data_ratings, on = 'movieId')
    movie_ratings = movie_ratings.groupby('title')['rating'].mean().sort_values(ascending = False).head(20)
    movie_ratings = movie_ratings.to_dict()
    '''
    complete the code to compute a variable movie_ratings
    1. perform a merge between data_movies and data_ratings.
    2. group by title and find the mean of ratings and fetch top 20 records.
    '''

    #######################################################################################################
    response = []

    for movie in movie_ratings:
        movie_record = data_movies[data_movies.title == movie].iloc[0]
        movie_poster =None
        response.append({
            "movieId": int(movie_record.movieId),
            "title": str(movie),
            "image": movie_poster if movie_poster != "nan" or movie_poster else default_poster_url,
            "genres": str(movie_record.genres).split("|"),
            "average_rating": movie_ratings[movie]
        })


    return {"status": True, "data": {"message": "Here are some of the popular recommendations.", "results" : response}}