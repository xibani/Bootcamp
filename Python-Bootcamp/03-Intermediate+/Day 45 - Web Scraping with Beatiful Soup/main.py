# from bs4 import BeautifulSoup
# import lxml
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
#
# print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)


# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("http://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup)
#
# articles = soup.find_all(name="a", class_="votelinks")
# articles_texts = []
# articles_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     articles_texts.append(text)
#     link = article_tag.get("href")
#     articles_links.append(link)
#
#
# article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# largest_number = max(article_upvote)
# print(article_upvote.index((largest_number)))
#
# print(articles_texts)
# print(articles_links)
# print(article_upvote)



## 100 Movies that You Must Watch

# Objective

# Scrape the top 100 movies of all time from a website. Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1).
# The result should look something like this:
#
# ```
# 1) The Godfather
# 2) The Empire Strikes Back
# 3) The Dark Knight
# 4) The Shawshank Redemption
# ... and so on
# ```
# The central idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles - from a website like Empire's (or from, say Timeout or Stacker that have curated similar lists).
#
# ### ⚠️ Important: Use the Internet Archive's URL
#
# Since websites change very frequently, **use this link**
# ```
# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# ```
# from the Internet Archive's Wayback machine. That way your work will match the solution video.
#
# (Do *not* use https://www.empireonline.com/movies/features/best-movies-2/ which I've used in the screen recording)
#
# # Solution
#
# You can find the code from my walkthrough and solution as a downloadable .zip file in the course resources for this lesson.



import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# requests para conseguir la pagina web y crear nuestra soup
response = requests.get(URL)
GM_100_web_page = response.text

soup = BeautifulSoup(GM_100_web_page, "html.parser")

greatest_movies_list = soup.find_all(name="h3", class_="title")

movies = [great_movie.getText().split(") ")[-1] for great_movie in greatest_movies_list]
greatest_movies = movies[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for i, movie in enumerate(greatest_movies):
        file.write(str(i) + ") " + movie + "\n")


