from bs4 import BeautifulSoup
import httpx

class NewsApp:
  """  This is class for News app """
  def __init__(self, query=None, words = None) -> None: 
    self.query = query
    self.words = words



  
  def getNewsTitles(self) -> dict:
    """ Gets the latest news Headlines """

    url = "https://www.bbc.com/news"
    
    html = httpx.get(url)
    soup = BeautifulSoup(html, 'html.parser')
                                  
    news_title_tag = soup.find_all("h3", class_="gs-c-promo-heading__title")
    news_title = []

    news_link_tag = soup.find_all("a", class_="gs-c-promo-heading")
    news_link = []

    for i in news_title_tag:
      news_title.append(i.text)

    for i in news_link_tag:
      i.find("a", href=True)
      news_link.append("https://www.bbc.com" + i["href"])

    titles = [i for i in news_title]
    links = [i for i in news_link]

    news_info = {"title": titles, "link": links}

    return news_info


  def getNewsAll(self, url:str) -> dict:
    """ This gets info from a news link given (of bbc only) """

    html = httpx.get(url)
    soup = BeautifulSoup(html, 'html.parser')

    if not url.startswith("https://www.bbc.com/news/"):
      return "Error: you have not entered the correct bbc url"
    else:
      html = httpx.get(url)
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