__author__ = 'Ankit_PC'
import urllib.request
import json
import re
from bs4 import BeautifulSoup
import pymongo


url = 'http://www.amazon.in/Google-Nexus-D821-16GB-Black/dp/B00GC1J55C/'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
#text = data.decode('utf-8')

soup=BeautifulSoup(data)
#To print in html format
#print (soup.prettify())
#print (json.dumps(soup))

#To find the product name
productTitle=soup.select("span#productTitle")[0].text
print (productTitle)

#To find the Price of particular product from Amazon.in
price=soup.select("span#priceblock_saleprice")[0].text
print (price.strip())

#To find the reviews from Amazon.in
reviews=soup.select("span#acrCustomerReviewText")[0].text
print (reviews)

#To find the rating from Amazon.in
rating=soup.select("div#avgRating > span")[0].text
print (rating.strip())

#To find the ASIN number of
#asin=soup.select("div.attrG > div.pdTab > td.value")[].text
#divTag = soup.find_all("div", {"class":"pdTab"})
#print (asin)


#text=soup.get_text()
#a=re.findall(r"B\w{9}", text)
#print (a)

#print(countDate)
d={}
d['productTitle']=productTitle.strip()
d['productPrice']=price.strip()
d['productReview']=reviews.strip()
d['productRating']=rating.strip()
#d['productASIN']=asin
json_string=json.dumps(d)
print (json_string)

#to get the text from website
#print(soup.get_text())

#Connection with mongoDB
MONGODB_URI = 'mongodb://localhost:27017/'
conn=pymongo.MongoClient(MONGODB_URI)

#Connect with database
db=conn.test

#Connect with collection
collection = db.my_collection

#Insert into collections
collection.insert_one(d)