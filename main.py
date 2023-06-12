from BobPyKit import Wikipedia, Anime, NewsApp


# wiki_app = Wikipedia(query="India")

# title, short_description, description, image_list = wiki_app.fetchResults()

# print(image_list)


# name, id, links = Anime().anime_search("Naruto")
# print(name)

news_app = NewsApp()
news = news_app.getNewsTitles()
print("\n".join(news['title']))