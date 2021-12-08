import aiohttp
from bs4 import BeautifulSoup

class NewsApp:
  """  This is class for News app """
  def __init__(self, query=None, words = None):
    self.query = query
    self.words = words



  """ This get the latest news Headlines """
  async def getNewsTitles(self):
    url = "https://www.bbc.com/news"
    
    async with aiohttp.ClientSession() as cs:
      async with cs.get(url) as r:
        html = await r.text()
    soup = BeautifulSoup(html, 'html.parser')
                                  
    news_title_tag = soup.find_all("h3", class_="gs-c-promo-heading__title")
    news_title = []

    news_link_tag = soup.find_all("a", class_="gs-c-promo-heading")
    news_link = []

    # fetching wanted material from the list of tags
    for i in news_title_tag:
      news_title.append(i.text)

    for i in news_link_tag:
      i.find("a", href=True)
      news_link.append("https://www.bbc.com" + i["href"])
    
    news_info = {"title" : [i for i in news_title], "link" : [i for i in news_link]}

    return news_info


  """ This gets info from a news link given (of bbc only) """
  async def getNewsAll(self, url:str):
    async with aiohttp.ClientSession() as cs:
      async with cs.get(url) as r:
        html = await r.text()
    soup = BeautifulSoup(html, 'html.parser')

    if not url.startswith("https://www.bbc.com/news/"):
      return "Error: you have not entered the correct bbc url"
    else:
      async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
          html = await r.text()
      soup = BeautifulSoup(html, 'html.parser')
      
      author = soup.find("p", class_="ssrcss-1rv0moy-Contributor").find("span").find("strong").text
      # can be none
      desc = soup.find_all("div", class_="ssrcss-uf6wea-RichTextComponentWrapper")
      desc_tag_list = []
      desc_list = []
      for i in range(len(desc)):
        if desc[i].find("p") == None:
          pass
        else:
          desc_tag_list.append(desc[i].find("p"))
      for i in desc_tag_list:
        desc_list.append(i.text)
      title = str(soup.find("title").text)[:-11]
      all_news_info = {"author": author, "title" : title, "description" : desc_list}
      return all_news_info