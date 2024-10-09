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
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}
    response = requests.get('https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    wordlist = soup.find('ul', class_='top-g')
    words = wordlist.find_all('li')
    # urls = [self._word_to_url(word) for word in words]
    urls = ['https://www.oxfordlearnersdictionaries.com/definition/english/abolish', 'https://www.oxfordlearnersdictionaries.com/definition/english/a_1']
    for url in urls:
      yield scrapy.Request(url, headers=headers)

  def parse(self, response):
    entry = response.css('div.entry')[0]
    name = entry.css('div.top-container h1::text').get()
    yield { 'entry': name }

