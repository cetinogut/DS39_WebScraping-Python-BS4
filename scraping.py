import requests # pulling data
from bs4 import BeautifulSoup # xml parsing
import json # exporting to files

# save function
def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)
        
# def save_function(article_list): # this is an another way of saving articles
#     with open('articles.txt', 'w') as f:
#         for a in article_list:
#             f.write(a+'\n')
#         f.close()

# scraping function
def ntv_breaking_news_rss():
    article_list = []

    try:
        # execute my request, parse the data using XML
        # parser in BS4
        r = requests.get('https://www.ntv.com.tr/son-dakika.rss') # ntv (turkish news channel -breaking news rss channel)
        print(r)
        #soup = BeautifulSoup(r.content, features='xml') # for xml feeds
        soup = BeautifulSoup(r.content, 'xml')

        # select only the "items" I want from the data
        #articles = soup.findAll('item') # for xml feed
        articles = soup.findAll('entry')

        # for each "item" I want, parse it into a list
        for a in articles:
            title = a.find('title').text
            #link = a.find('link').text # for xml feed
            link = a.find('id').text
            #published = a.find('pubDate').text # for xml feed
            published  = a.find('published').text

            # create an "article" object with the data
            # from each "item"
            article = {
                'title': title,
                'link': link,
                'published': published
                }
            # append my "article_list" with each "article" object
            article_list.append(article)
        
        # after the loop, dump my saved objects into a .txt file
        print(article_list)
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)

print('Starting scraping')

ntv_breaking_news_rss()

print('Finished scraping')