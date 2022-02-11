import requests
from bs4 import BeautifulSoup


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features"
                        "/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
# GET LIST OF MOVIES
movies_section = soup.find(name="div", class_="entity-info-items__list")
movie_list = [movie.getText() for movie in movies_section.find_all("li")]
movie_list.reverse()
print(movie_list)

with open("top_100_movies.txt", "a") as file:
    num = 0
    for item in movie_list:
        num += 1
        file.write(f"{num}: {item}\n")





