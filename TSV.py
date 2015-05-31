import pymongo

__author__ = 'Ankit_PC'
MONGODB_URI = 'mongodb://localhost:27017/'
conn=pymongo.MongoClient(MONGODB_URI)

#Connect with database
db=conn.test

#Connect with collection
amazon = db.my_collection

snapdeal=db.snapdeal
redmi=db.MicromaxA24Mobile
date=["05/25/15","05/26/15","05/27/15","05/28/15"]

amazon_data=amazon.find({'productTitle':'Micromax Bolt A24 (Champange)'}).sort("date",pymongo.ASCENDING)
snapdeal_data=snapdeal.find({'productTitle':'Micromax A24 Mobile Phone'}).sort("date",pymongo.ASCENDING)

for d in date:
    black={}
    black['date']=d
    black['name']="Micromax A24 Mobile"
    for a in amazon_data:
        if d==a['date']:
            a['productPrice']=a['productPrice'].replace(",","")
            a['productPrice']=a['productPrice'].replace(".00","")
            black['Amazon']=a['productPrice']
            black['AmazonReviews']=a['productReview']
        break
    for s in snapdeal_data:
        if d==s['date']:
            tmp=s['productPrice'].replace("Rs   ","")
            black['Snapdeal']=tmp
            rev=s['productReview'].replace('(',"")
            rev=rev.replace(')',"")
            black['SnapdealReviews']=rev
        break
    redmi.insert_one(black)