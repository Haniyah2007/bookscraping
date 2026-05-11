import requests  # same library you used in your book scraper!

# Your TMDB API key - sign up free at themoviedb.org to get this
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# The URL we're sending our request to
# Think of this like the "menu" we're handing to the waiter
url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

# Send the request - same as your scraper!
response = requests.get(url)

# .json() converts the response into a Python dictionary
data = response.json()

# "results" is a list of movies inside the dictionary
movies = data["results"]

# Loop through and print each movie - just like "for book in books"!
for movie in movies:
    title = movie["title"]
    
    rating = movie["vote_average"]
    overview = movie["overview"]  # short description of the movie
    
    print(f"Title: {title}")
    print(f"Rating: {rating}/10")
    print(f"Overview: {overview}")
    print("-" * 50)  # just a divider line to separate movies