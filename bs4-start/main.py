from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

data = response.text

soup = BeautifulSoup(data, 'html.parser')

h3_title_tags = soup.select(selector=".article-title-description h3")

titles = [h3.get_text() for h3 in h3_title_tags]
print(titles)

with open("movie_list.txt", mode="w", encoding="utf-8") as top_movie_list:
    for title in reversed(titles):
        top_movie_list.write(f"{title}\n")