# Movie Recommendation System

This project implements a movie recommendation system using Streamlit for the user interface and TMDb (The Movie Database) API for fetching movie posters. It leverages precomputed similarity data to recommend movies similar to the one selected by the user.

## Features

- **Movie Search**: Allows users to select a movie from a list.
- **Recommendations**: Provides top 10 movie recommendations based on the selected movie.
- **Posters**: Displays movie posters alongside recommendations for a better visual experience.

## Dependencies

- `pandas` for data manipulation
- `streamlit` for creating the web app interface
- `pickle` for loading precomputed data
- `tmdbv3api` for accessing movie posters from TMDb

## Setup

1. **Install Dependencies**:

    ```bash
    pip install pandas streamlit pickle5 tmdbv3api
    ```

2. **API Key**:
   
   Replace `'bf49392cc5a7db79873193791c6c5701'` with your TMDb API key. You can obtain an API key by signing up at [TMDb API](https://www.themoviedb.org/documentation/api).

3. **Data Files**:

   Ensure you have the following files in your project directory:
   - `movies.pkl`: Pickle file containing the movie dataset.
   - `similarity.pkl`: Pickle file containing the precomputed similarity matrix.

## How to Run

1. Save the code in a file named `app.py`.
2. Run the Streamlit app using:

    ```bash
    streamlit run app.py
    ```

3. Open the provided local URL in your browser to use the app.

## Code Overview

- **`fetch_poster(movie_title)`**: Retrieves the poster URL for a given movie title using TMDb API.
- **`recommend(movie)`**: Provides movie recommendations based on the selected movie. It uses precomputed similarity data to find and rank similar movies.
- **Streamlit Interface**:
  - **Selectbox**: Allows users to choose a movie for recommendations.
  - **Recommendation Display**: Shows top 10 recommended movies with their posters.

## Error Handling

- **Data Loading**: If the data files (`movies.pkl`, `similarity.pkl`) cannot be loaded, an error message will be displayed.
- **Column Check**: The app checks for the presence of the 'orig_title' column in the dataset and displays an error if it's missing.

## Contributing

Feel free to fork this repository and submit pull requests. Contributions and suggestions are welcome!

