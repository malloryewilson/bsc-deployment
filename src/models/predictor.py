import pandas as pd
ratings_dataframe = pd.read_csv('dataframe.csv')
ratings_matrix = pd.read_csv('ratings_matrix.csv')

def get_prediction(movie_name):
    """ Given a list of feature values, return a prediction made by the model"""
    
    #loaded_model = un_pickle_model()
    
    user_ratings = rating_matrix[movie_name]
    correlation_with_movie = pd.DataFrame(rating_matrix.corrwith(user_ratings))
    correlation_with_movie = correlation_with_movie.join(ratings_dataframe['# of ratings'])
    correlation_with_movie.columns = [f'Corr. With {movie_name}', '# of Ratings']
    correlation_with_movie.index.names = ['Movie Title']
    return correlation_with_movie[correlation_with_movie['# of Ratings'] > 50].sort_values(f'Corr. With {movie_name}', ascending = False).iloc[1:,:].head(10)

    # Model is expecting a list of lists, and returns a list of predictions
    predictions = loaded_model.predict(feature_values)
    # We are only making a single prediction, so return the 0-th value
    return predictions[0]

def un_pickle_model():
    """ Load the model from the .pkl file """
    with open("src/models/model.pkl", "rb") as model_file:
        loaded_model = pickle.load(model_file)
    return loaded_model