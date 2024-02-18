# Quiz045



# 1. UML Diagram

<img width="341" alt="Screenshot 2024-02-18 at 18 10 04" src="https://github.com/Rokyyz/Unit3/assets/134658259/3acd3cbb-e48b-4787-b5b5-d4f27c0fe1c8">


# 2. solutions

```.py
from mon_8_jan.my_lib import DatabaseWorker
haiku = """Code flows like a stream
algorithms guide its way
In silence, it solves"""

#Create Database with table Words
db_name = "quiz_046.db"
db = DatabaseWorker(db_name)

query = """CREATE TABLE if not exists Words(
    id INTEGER PRIMARY KEY,
    length INTEGER,
    words VARCHAR(256) not null
    )"""
db.run_query(query)

average = """ select avg(length) from Words"""

results = db.search(average)

#close database
print(f"average word length is, {results[0]:.2f}")

                                                                                                                                                                                                      
```


# 3. proof of work

<img width="1440" alt="Screenshot 2024-02-18 at 18 08 25" src="https://github.com/Rokyyz/Unit3/assets/134658259/d52d3156-5bbd-4559-acfd-705e9d1a9d76">
