import aiohttp
from bs4 import BeautifulSoup

class Wikipedia:
  def __init__(self, query, words = None):
    self.query = query
    self.words = words
  
  """Made a method to generate results but it should idealy call something else, fetch 
  result method shoud be used in case no page/results for the passed query is found please check later"""
  async def fetchResults(self):

    async with aiohttp.ClientSession() as cs:
      async with cs.get(f"https://en.wikipedia.org/wiki/{self.query}") as r:
        html = await r.text()

    soup = BeautifulSoup(html, 'html.parser')
    description_len = len(soup.find_all("p"))
    description_list = []
    image_list = []

    try:
      short_description = soup.find(class_="shortdescription").text

      for i in range(0, description_len):
        desc_for = soup.find_all("p")[i].text
        description_list.append(desc_for)
        description = ["".join(description_list)]
        title = soup.find("h1", id="firstHeading").text

      image_tag = soup.find_all("a", class_="image", href=True)
      for i in image_tag:
        image_list.append("https://en.wikipedia.org" + i["href"])

      if self.words != None:
        return title, short_description, str(description[0])[:self.words], image_list
      else:
        return title, short_description, str(description[0]), image_list

    except Exception as e:
      raise e