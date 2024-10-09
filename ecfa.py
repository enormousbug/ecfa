from bs4 import BeautifulSoup
import requests
import scrapy

class OxfrodLearners5000Spider(scrapy.Spider):
  name = 'OxfrodLearnersSpider'

  def _word_to_url(self, word):
    link = word.find('a')
    href = link.get('href')
    return 'https://www.oxfordlearnersdictionaries.com' + href

  def start_requests(self):
    response = requests.get(
      'https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000',
      headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}
      )
    soup = BeautifulSoup(response.content, 'html.parser')
    wordlist = soup.find('ul', class_='top-g')
    words = wordlist.find_all('li')
    urls = [self._word_to_url(word) for word in words]
    for url in urls:
      yield scrapy.Request(url)

  def parse(self, response):
      pass
