# Movie Recommender System

This project is a Streamlit-based web application that recommends movies based on user selection. It uses content-based filtering to suggest similar movies to the one selected by the user.

## Features

- User-friendly interface built with Streamlit
- Movie selection from a dropdown menu
- Displays 20 movie recommendations with movie posters
- Utilizes The Movie Database (TMDb) API for fetching movie posters

## Installation

1. Clone this repository:
   \`\`\`
   git clone https://github.com/adityarathore622/movie-recommender-system.git
   cd movie-recommender-system
   \`\`\`

2. Install the required packages:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

3. Obtain an API key from [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api) and replace \`YOUR_API_KEY\` in the \`app.py\` file with your actual API key.

## Usage

1. Run the Streamlit app:
   \`\`\`
   streamlit run app.py
   \`\`\`

2. Open your web browser and go to \`http://localhost:8501\` (or the URL provided in the terminal).

3. Select a movie from the dropdown menu and click "Show Recommendation" to see similar movies.

## How it Works

1. The app loads pre-processed movie data and a similarity matrix from pickle files.
2. When a user selects a movie, the app finds the most similar movies based on the similarity matrix.
3. The app then fetches movie posters for the recommended movies using the TMDb API.
4. Finally, it displays the top 20 recommended movies with their titles and posters.

## Data Files

- \`movie_list.pkl\`: Contains the list of movies with their details.
- \`similarity.pkl\`: Contains the similarity matrix used for recommendations.

Make sure these files are present in the same directory as \`app.py\`.

## Dependencies

- streamlit
- requests
- pickle


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgements

- Movie data and posters provided by [The Movie Database (TMDb)](https://www.themoviedb.org/)
- Built with [Streamlit](https://streamlit.io/)

