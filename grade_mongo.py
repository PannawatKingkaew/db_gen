import pandas as pd
import pymongo
import random
import time
from random import randrange
from tqdm import tqdm

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["grade"]

def gen(row):
    size = 0
    i = 0
    mongo_docs = []
    pbar = tqdm(total = row)
    while(size < row):
            StuID = "620" + str(randrange(1000000000,9999999999))
            SubID = random.choice(["010123102","010123103","010123105","010113010","010113011","040313005","040313007","040313008","040313006","080103001"])
            G = random.choice(["A","B+","B","C+","C","D+","D","F"])
            mydict = { "StudentID": StuID,"SubjectID": SubID,"Grade": G}
            mongo_docs += [mydict]
            pbar.update()
            i+=1
            size +=1
            if i == 5000000:
                mycol.insert_many(mongo_docs)
                mongo_docs = []
                i =0
    mycol.insert_many(mongo_docs)
      
start = time.time()
gen(120000000) ##10GB
end = time.time()
print(end-start)
