import csv
import pymongo

MONGODB_URI = 'mongodb://localhost:27017/'
conn=pymongo.MongoClient(MONGODB_URI)

#Connect with database
db=conn.test

#Connect with collection
redmi = db.MicromaxA24Mobile

results=redmi.find()

with open('MicromaxA24Mobile.tsv','wb') as csvfile:
    fieldnames = ['date', 'AmazonPrice', 'SnapdealPrice']
    print (fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for re in results:
       writer.writerow({'date': re['date'], 'AmazonPrice': re['Amazon'], 'SnapdealPrice': re['Snapdeal']})

result=redmi.find()

with open('MicromaxA24Mobile Reviews.tsv','wb') as csvfile:
    fieldnames = ['date', 'AmazonReview', 'SnapdealReview']
    print (fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    for r in result:
        print(r['AmazonReviews'])
        writer.writerow({'date': r['date'], 'AmazonReview': r['AmazonReviews'], 'SnapdealReview': r['SnapdealReviews']})