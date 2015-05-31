import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json
import time
import pymongo

driver = webdriver.Firefox()
driver.get("http://www.amazon.in/")
assert "Amazon" in driver.title
# driver.maximize_window()
elem = driver.find_element_by_id("twotabsearchtextbox")
elem.send_keys("smartphones")
elem.send_keys(Keys.RETURN)

# url = driver.current_url
# print (url)
# response = urllib.request.urlopen(url)
# data = response.read()      # a `bytes` object
source=driver.page_source
#print (source)
soup=BeautifulSoup(source)
#print (soup.prettify())

MONGODB_URI = 'mongodb://localhost:27017/'
conn=pymongo.MongoClient(MONGODB_URI)

#Connect with database
db=conn.test

#Connect with collection
collection = db.my_collection


for i in range(1,20):
    print (i)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[1]/div/div/div[2]/div/div/span[1]/div').click()
    except:
        print( "NoSuchElementException")
    time.sleep(5)
    productTitle = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li/div/div[2]/div[1]/a/h2')
    if len(productTitle) == 0:
        productTitle = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[3]/ul/li/div/div/div/div[2]/div[1]/a/h2')

    print(len(productTitle))
    # for product in productTitle:
    #     print(product.text)
#vertical /html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li[1]/div/div[2]/div[1]/a/h2
#horizontal /html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/ul/li[1]/div/div/div/div[2]/div[1]/a/h2

    price = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li/div/div[3]/div[1]/a/span')
    if len(price) == 0:
        price = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[3]/ul/li/div/div/div/div[2]/div[2]/div[1]/div[1]/a/span')

    print(len(price))
    # for amount in price:
    #     print(amount.text)
# /html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/ul/li[1]/div/div[3]/div[1]/a/span
# /html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[3]/ul/li/div/div/div/div[2]/div[2]/div[1]/div[1]/a/span

        # To find the reviews from Amazon.in
    reviews = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li/div/div[5]/a')
    if len(reviews) == 0:
        reviews = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[3]/ul/li/div/div/div/div[2]/div[2]/div[2]/div[1]/a')
    # for review in reviews:
    #     print(review.text)
    print  (len(reviews))
# /html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[2]/ul/li[1]/div/div[5]/a
# /html/body/div[1]/div[1]/div[4]/div[2]/div/div[2]/div[3]/ul/li/div/div/div/div[2]/div[2]/div[2]/div[1]/a

        # To find the rating from Amazon.in
    # ratings= driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div/div[1]/span')
    # for rating in ratings:
    #     print(rating.text)

    for prod, amount, review in zip(productTitle, price, reviews):
        d={}
        d['productTitle']=prod.text
        d['productPrice']=amount.text.strip()
        d['productReview']=review.text
        d['date']=time.strftime("%x")
        collection.insert_one(d)
        print(d)


    flag = False # Keep trying untill page loads and the element is found.

    while flag == False:
        try:
            i_ele = driver.find_element_by_id('pagnNextString')
            i_ele.click()
            flag = True
            print ("Element clicked")
        except:
            print ("Element not clicked")

