import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from django.http import HttpResponse
from .models import Accessory


def scrap(*args):
    titles=[]
    prices=[]
    all_reviews=[]
    total_reviews=[]


    pages = np.arange(1, 2, 1)
    for page in pages:
        url = "https://www.jumia.ma/ordinateurs-accessoires-informatique/?page=" + str(page)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all = soup.find_all('div', class_='info')

        for single in all:
            title = single.find('h3', class_="name").text
            price = single.find('div', class_="prc").text
            reviews = single.find_all('div', class_="rev")
            for single_item in reviews:
                review = single_item.find('div', class_="stars").text
                total_review = single_item.text
                prices.append(price)
                titles.append(title)
                all_reviews.append(review)
                total_reviews.append(total_review)
                accessory = Accessory(title=title, price=price, all_review=review, total_review=total_review)
                accessory.save()


    df = pd.DataFrame({
        "Price":prices,
        "Title":titles,
        "Reviews":all_reviews,
        "Total reviews" : total_reviews
    })

    df.to_csv('./books/jumia.csv')

    response = HttpResponse()
    response.headers['Status'] = 200
    return response


scrap()


