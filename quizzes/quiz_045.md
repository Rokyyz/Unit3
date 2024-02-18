# Quiz045



# 1. UML Diagram

<img width="341" alt="Screenshot 2024-02-18 at 18 10 04" src="https://github.com/Rokyyz/Unit3/assets/134658259/3acd3cbb-e48b-4787-b5b5-d4f27c0fe1c8">


# 2. solutions

```.py
import sqlite3
from mon_8_jan.my_lib import DatabaseWorker
haiku = """Code flows like a stream
algorithms guide its way
In silence, it solves"""

# Create Database with table Words
db_name = "quiz_046.db"
db = DatabaseWorker(db_name)

query = """CREATE TABLE if not exists Words(
    id INTEGER PRIMARY KEY,
    length INTEGER,
    words not null
    )"""
db.run_query(query)

for word in haiku.split():
    querytwo = f"INSERT INTO Words(words, length)values ('{word}',{len(word)}) "
    db.insert(querytwo)

querythree=""" SELECT avg(length) FROM Words;"""
db.run_query(querythree)

average = """SELECT AVG(length) FROM Words"""

results = db.search(average)

if results is not None and results[0] is not None:
    print(f"average word length is, {results[0]:.2f}")
else:
    print("No data found.")                                                                                                                                                                                    
```


# 3. proof of work

<img width="1440" alt="Screenshot 2024-02-18 at 21 34 31" src="https://github.com/Rokyyz/Unit3/assets/134658259/e9923c74-6885-4929-9a32-42a681c8d2aa">

