import psycopg2
import psycopg2.extras
import random
from random import randrange
import time
from tqdm import tqdm

conn = psycopg2.connect(
   database="mint", user='mint', password='Keiz1159', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Student (StudentID TEXT, SubjectID TEXT, Grade TEXT)")        
conn.commit()


def gen(row):
      size = 0
      i = 0
      docs = []
      pbar = tqdm(total = row)
      while(size < row):
            StuID = "620" + str(randrange(1000000000,9999999999))
            SubID = random.choice(["010123102","010123103","010123105","010113010","010113011","040313005","040313007","040313008","040313006","080103001"])
            G = random.choice(["A","B+","B","C+","C","D+","D","F"])
            mydict = { "StudentID": StuID,"SubjectID": SubID,"Grade": G}
            docs += [mydict]
            pbar.update()
            i+=1
            size +=1
            if i == 5000000:
                  psycopg2.extras.execute_batch(cur, "INSERT INTO Student (StudentID, SubjectID, Grade) VALUES (%(StudentID)s, %(SubjectID)s, %(Grade)s);",docs)
                  conn.commit()
                  docs = []
                  i =0
      conn.commit()



start = time.time()
gen(190000000) ##10GB
end = time.time()
print(end-start)
