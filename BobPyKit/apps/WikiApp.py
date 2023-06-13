from bs4 import BeautifulSoup
import httpx

class Wikipedia:
  """ A Wikipedia Scrapper """
  def __init__(self, query, words = None) -> None:
    self.query = query
    self.words = words
  

  def fetchResults(self) -> dict:
    """ Searches for the query on wikipedia and returns data"""
    
    html = httpx.get(f"https://en.wikipedia.org/wiki/{self.query}")
    soup = BeautifulSoup(html, 'html.parser')

    description_len = len(soup.find_all("p"))
    description_list = []
    image_links = []

    try:
      short_description = soup.find(class_="shortdescription").text

      for i in range(0, description_len):
        desc_for = soup.find_all("p")[i].text
        description_list.append(desc_for)
        description = ["".join(description_list)]
        title = soup.find("h1", id="firstHeading").text

      image_tag = soup.find_all("a", class_="image", href=True)
      for i in image_tag:
        image_links.append("https://en.wikipedia.org" + i["href"])

      if self.words != None:
        data = {"title": title, "short_description": short_description, "description": str(description[0])[:self.words], "image_links": image_links}
        return data
      else:
        data = {"title": title, "short_description": short_description, "description": str(description[0]), "image_links": image_links}
        return data

    except Exception as e:
      raise e