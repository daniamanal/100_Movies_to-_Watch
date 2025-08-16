import requests
from bs4 import BeautifulSoup

url = ("https://web.archive.org/web/20200518073855/"
       "https://www.empireonline.com/movies/features/best-movies-2/")  # why 2 http in url?
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
all_h3 = soup.select("h3.title")
# print (all_h3)
movie_list = [tag.getText() for tag in all_h3]  # new_list = [new_items for items in list]
# print(movie_list)
with open("movies.txt", "w", encoding="utf-8") as file:
    for n in range(len(movie_list) -1, -1, -1):
        title = movie_list[n]
        file.write(title + "\n")
