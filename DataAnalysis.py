import statistics
import pymongo
MONGODB_URI = 'mongodb://localhost:27017/'
conn=pymongo.MongoClient(MONGODB_URI)

#Connect with database
db=conn.test

#Connect with collection
collection = db.my_collection

#total=collection.find({'productPrice': '5499.00'})
total=collection.find({'productTitle':'KARBONN TITANIUM S3 512MB / 4GB (White)'})

black=[]
for text in total:
    print(text['productPrice'])
    temp = str(text['productPrice'])
    black.append(float(temp))
print ('This is the array of productPrices for the desired product')
print(black)



print ('This is the length of the printed array')
print (len(black))



print ('Mean price for all the sample product will be:---->>>>>:',statistics.mean(black))


print ('Median price for all the sample product will be:---->>>>>:',statistics.median(black))


print ('Standard Deviation price for all the sample product will be:---->>>>>:',statistics.stdev(black))


