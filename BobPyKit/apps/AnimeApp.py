import httpx
from bs4 import BeautifulSoup

class Anime:
  """ Search for anime on MyAnimeList """
  def __init__(self):

    self.anime_URL = "https://myanimelist.net/anime.php?q={query}&cat=anime"
    self.manga_URL = "https://myanimelist.net/manga.php?q={query}&cat=manga"
    # self.character_URL = "https://myanimelist.net/character.php?q={query}&cat=character"


  def anime_search(self, anime:str):
    url = self.anime_URL.format(query=anime)
    
    html = httpx.get(url)
    soup = BeautifulSoup(html, 'html.parser')

    anchor = soup.find_all("a", class_="hoverinfo_trigger fw-b fl-l")

    name = [x.text for x in anchor]
    _id = [x['id'].strip("sinfo") for x in anchor]
    links = [x['href'] for x in anchor]

    return name, _id, links

