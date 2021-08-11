from flask import Flask, send_from_directory, render_template, request, redirect, url_for
from waitress import serve
import numpy as np
import pandas as pd
from src.utils import extract_feature_values
from src.models.predictor import get_prediction

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index.html")

@app.route("/make_prediction", methods=["POST"])
def make_prediction():
    """ Use the ML model to make a prediction using the form inputs. """
    # Get the data from the submitted form
    movie_name = request.form['movie_title']


    # Convert the data into just a list of values to be sent to the model
#     feature_values = extract_feature_values(data)
#     print(feature_values) # Remove this when you're done debugging

    # Send the values to the model to get a prediction
    

    # Tell the browser to fetch the results page, passing along the prediction
    return redirect(url_for("show_results", movie_name=movie_name))

@app.route("/show_results")
def show_results():
    """ Display the results page with the provided prediction """
    
    movie_name = request.args.get('movie_name')
    
    prediction = get_prediction(movie_name)
    # Extract the prediction from the URL params
#     prediction = request.args.get("prediction")

    # Return the results pge
    return render_template("results.html", prediction=prediction)


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
