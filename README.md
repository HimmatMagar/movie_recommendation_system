# Movie Recommendation System

A comprehensive movie recommendation system built with FastAPI backend and a modern HTML/CSS/JavaScript frontend. The system uses collaborative filtering and content-based filtering to provide personalized movie recommendations.

## Features

- **Smart Recommendations**: Get movie suggestions based on movie titles, genres, or keywords
- **FastAPI Backend**: High-performance asynchronous API built with Python
- **Modern Frontend**: Responsive UI with gradient backgrounds, glassmorphism effects, and smooth animations
- **Flexible Search**: Search by movie name, genre, actor, or director
- **Data-Driven**: Built on TMDB 5000 movie dataset with advanced NLP processing
- **Real-time Responses**: Instant recommendations via REST API
- **CORS Enabled**: Ready for integration with any frontend application

## Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Python 3.12**: Core programming language
- **Scikit-learn**: Machine learning for similarity computation
- **Pandas & NumPy**: Data manipulation and analysis
- **Pickle**: Model serialization

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom animations, gradients, and glassmorphism effects
- **Vanilla JavaScript**: DOM manipulation and API communication
- **Fetch API**: Async HTTP requests to backend

### Data Processing
- **NLTK**: Text preprocessing and stemming
- **CountVectorizer**: Feature extraction from movie tags
- **Cosine Similarity**: Recommendation algorithm

## Project Structure

```
movie_recommendation_system/
│
├── api/
│   ├── app.py              # FastAPI application
│   ├── movies.pkl          # Preprocessed movie data
│   └── similarity.pkl      # Precomputed similarity matrix
│
├── frontend/
│   └── index.html          # Main frontend interface
│
├── notebook/
│   └── research.ipynb      # Jupyter notebook for data exploration and model building
│
├── data/                   # Raw datasets (TMDB 5000 movies and credits)
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
│
├── artifact/               # Generated model artifacts
│   ├── movies.pkl
│   └── similarity.pkl
│
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Installation Guide

### Prerequisites
- Python 3.12 or higher
- Git (for cloning the repository)
- Internet connection (to download dependencies)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd movie_recommendation_system
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # Using conda (recommended)
   conda create -p venv python==3.12 -y
   conda activate venv/
   
   # Alternatively, using venv
   # python -m venv venv
   # venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Required Data**
   The project requires the TMDB 5000 dataset. Place the following files in the `data/` directory:
   - `tmdb_5000_credits.csv`
   - `tmdb_5000_movies.csv`
   
   You can download them from [Kaggle TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

5. **Generate Model Artifacts**
   Run the research notebook to generate the required pickle files:
   ```bash
   jupyter notebook notebook/research.ipynb
   ```
   Execute all cells in the notebook to generate:
   - `artifact/movies.pkl`
   - `artifact/similarity.pkl`

## Usage Instructions

### Starting the Backend Server
```bash
# From the project root directory
uvicorn api.app:app --reload
```
The API will be available at `http://127.0.0.1:8000`

### Accessing the Frontend
1. Open `frontend/index.html` in your web browser, or
2. Start a simple HTTP server in the frontend directory:
   ```bash
   cd frontend
   python -m http.server 8080
   ```
   Then visit `http://127.0.0.1:8080`

### Using the API Directly
The FastAPI backend provides the following endpoints:

- **GET /** - Root endpoint with welcome message
- **GET /health** - Health check endpoint
- **POST /recommend** - Get movie recommendations

#### Example Recommendation Request
```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
  -H "Content-Type: application/json" \
  -d '{"movie_name": "Inception"}'
```

#### Expected Response
```json
{
  "movie": "Inception",
  "recommendation": [
    "Interstellar",
    "The Dark Knight",
    "Memento",
    "Shutter Island",
    "The Prestige"
  ]
}
```

## Frontend Usage

1. Enter a movie title, genre, actor name, or keyword in the search box
2. Click the "Recommend" button or press Enter
3. View the generated movie recommendations in the grid below
4. Each recommendation card shows:
   - Movie title
   - Release year
   - Genre
   - Rating (when available)
   - Brief description

## API Documentation

Once the server is running, visit:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

These interfaces provide interactive documentation for all available endpoints.

## Model Details

The recommendation system uses a content-based filtering approach:

1. **Feature Engineering**: Combines movie overview, genres, cast, crew, and keywords into a single "tag" field
2. **Text Preprocessing**: 
   - Lowercasing
   - Tokenization
   - Stemming (Porter Stemmer)
   - Stop word removal
3. **Vectorization**: Convert text features to numerical vectors using CountVectorizer
4. **Similarity Calculation**: Compute cosine similarity between all movie pairs
5. **Recommendation**: For a given movie, find the top 5 most similar movies

## Data Sources

- **TMDB 5000 Movie Dataset**: Contains information about 5000 movies from The Movie Database (TMDB)
  - Includes metadata like budget, revenue, release dates, genres, production companies, etc.
  - Source: [Kaggle TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- TMDB for providing the movie dataset
- The open-source community for the fantastic libraries used
- Inspired by various movie recommendation tutorials and courses

---

**Enjoy discovering your next favorite movie!** 🍿