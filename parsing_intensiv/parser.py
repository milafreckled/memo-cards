from bs4 import BeautifulSoup
from random import randint
import requests
import time
def parse_the_page(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    allAs = soup.findAll('a', attrs={})
    allLists = soup.findAll('ul')
    values = soup.findAll('div', attrs={'itemprop': 'review'})    
    
    for value in values:
        author_tag = value.find('meta', attrs={'itemprop': 'author'})
        print(author_tag['content'])
        date_tag = value.find('meta', attrs={'itemprop': 'datePublished'})
        print(date_tag['content'])
        description_tag = value.find('meta', attrs={'itemprop': 'description'})
        description_tag = description_tag
        print(description_tag['content'])
        rating_tag = value.find('div', attrs={'itemprop': 'reviewRating'})
        print(rating_tag.meta['content'])
        
def get_next_page_url(html_data):
    soup = BeautifulSoup(html_data, 'lxml') 
    tag = soup.find('a', attrs = {'aria-label': 'Следущая страница'})
    if tag is None:
        return None
    else:
        return 'https://market.yandex.ru'+tag['href']
    
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'is_gdpr=0; is_gdpr_b=CKfTFRCzMg==; i=YzYerGoyrVtVATHbh1O+6UDWjbIZjot2/rYMmFSThy1IYPsWo27VgspGMkPvhu8wyYiN9SCpWELfhPcsbq4F2sNKfxc=',
    'Host': 'market.yandex.ru',
    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '2',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36'
    }
url = "https://market.yandex.ru/product--smartfon-apple-iphone-12-128gb/722974019/reviews?track=tabs"

while True:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    data = response.text
    parse_the_page(data)
    time.sleep(randint(10, 20))
    url = get_next_page_url(data)
    if url is None:
        break



        

                        
