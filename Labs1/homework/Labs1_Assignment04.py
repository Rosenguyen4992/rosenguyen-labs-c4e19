from pymongo import MongoClient


uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Connect to database
client = MongoClient(uri)

#2. Get database
db = client.get_default_database()

#3. Get collection
customers = db['customers']

#4. Count by refs

all_customer = customers.find()

ref_event = 0
ref_wom = 0
ref_ads = 0

for customer in all_customer:
    if customer['ref'] == 'events':
        ref_event += 1
    elif customer['ref'] == 'wom':
        ref_wom += 1
    else:
        ref_ads += 1
print("Number of customers acquired by events, wom and ads are respectively are: {0}, {1}, {2}.".format(ref_event, ref_wom, ref_ads))

#5. Draw the chart 
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

#5.1. Prepare data
labels = ['Events', 'Wom', 'Ads']
values = [ref_event, ref_wom, ref_ads]
colors = ["red", "blue", 'yellow']

#5.2. Plot

pyplot.pie(values, labels = labels, colors = colors)
pyplot.axis("equal")

#5.3. Show
pyplot.show()