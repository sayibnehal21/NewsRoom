from http import client
from os import times
from pydoc import cli
from time import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

if __name__ == "__main__":
    sitemap = requests.get("https://www.moneycontrol.com/news/news-sitemap.xml")
    sitemap_soup = BeautifulSoup(sitemap.text, 'lxml')

    news_links = [link.text for link in sitemap_soup.select("loc")]


    client = MongoClient("mongodb://admin:password@3.82.214.186:27017")
    db = client['newsweb']

    collection = db['articles']

    # myquery = {'publisher': 'moneycontrol'}
    # x = collection.delete_many(myquery)
    # print(x.deleted_count)
    # print(x)
    for link in news_links:
        try:
            resp = requests.get(link)

            soup = BeautifulSoup(resp.text, 'lxml')

            subject = soup.select("h1")[0].text.strip()
            author = soup.select("div.article_author")[0].text.strip()
            timestamp = soup.select("div.article_schedule")[0].text.strip()
            body = soup.select("div.content_wrapper")[0].text.strip()
            publisher = "moneycontrol"
            id = str(link.split(".")[-2].split("-")[-1]) + "_moneycontrol"

            data = {
                'subject': subject,
                'author': author,
                'timestamp': timestamp,
                'body': body,
                'publisher': publisher,
                '_id': id,
                'url': link
            }

            collection.insert_one(data)


        except Exception as e:
            continue

