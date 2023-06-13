import httpx
from bs4 import BeautifulSoup


class Anime:
    """ MyAnimeList Scrapper """

    def __init__(self) -> None:

        self.anime_URL = "https://myanimelist.net/anime.php?q={query}&cat=anime"
        self.manga_URL = "https://myanimelist.net/manga.php?q={query}&cat=manga"
        # self.character_URL = "https://myanimelist.net/character.php?q={query}&cat=character"

    def anime_search(self, anime: str = None) -> dict:
        """ Searches MyAnimeList for anime """

        if anime == None:
            return 'No anime name provided'
        url = self.anime_URL.format(query=anime)

        html = httpx.get(url)
        soup = BeautifulSoup(html, 'html.parser')

        anchor = soup.find_all("a", class_="hoverinfo_trigger fw-b fl-l")

        name = [x.text for x in anchor]
        _id = [x['id'].strip("sinfo") for x in anchor]
        links = [x['href'] for x in anchor]

        _dict = {"name": name, "id": _id, "links": links}

        return _dict
