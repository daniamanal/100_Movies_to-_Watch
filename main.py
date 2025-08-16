import requests
from bs4 import BeautifulSoup

url = ("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")  
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
all_h3 = soup.select("h3.title")

movie_list = [tag.getText() for tag in all_h3]  # new_list = [new_items for items in list]

with open("Top_100_Movies.txt", "w", encoding="utf-8") as file:
    for n in range(len(movie_list) -1, -1, -1):
        title = movie_list[n]
        file.write(title + "\n")

