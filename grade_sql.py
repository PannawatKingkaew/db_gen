import sqlite3
import random
from random import randrange
import time
from tqdm import tqdm

conn = sqlite3.connect('grade.db') 
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Student (StudentID TEXT, SubjectID TEXT, Grade TEXT)")        
conn.commit()


def gen(row):
      size = 0
      i = 0
      pbar = tqdm(total = row)
      while(size < row):
            StuID = "620" + str(randrange(1000000000,9999999999))
            SubID = random.choice(["010123102","010123103","010123105","010113010","010113011","040313005","040313007","040313008","040313006","080103001"])
            G = random.choice(["A","B+","B","C+","C","D+","D","F"])
            cur.execute("INSERT INTO Student (StudentID, SubjectID, Grade) VALUES (?, ?, ?)",(StuID, SubID, G))
            pbar.update()
            i+=1
            size +=1
            if i == 5000000:
                  conn.commit()
                  i =0
      conn.commit()



start = time.time()
gen(295000000) ##10GB
end = time.time()
print(end-start)
