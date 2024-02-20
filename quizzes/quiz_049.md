## quiz_049

1. Diagram

![CommSci 35](https://github.com/Rokyyz/Unit3/assets/134658259/c9242d5e-f648-4b76-b6cc-de6576e0e90f)


2. Solution

```.py
from mon_8_jan.my_lib import DatabaseWorker
x = DatabaseWorker("bitcoin_exchange.db")

create_user = """ CREATE TABLE IF NOT EXISTS users(
    id integer PRIMARY KEY
    name text NOT NULL
    email text NOT NULL)"""

insert_query = """ INSERT INTO users (id, name, email) VALUES (920,'bob','bob@gmail.com'),
(560, 'alice', 'alice@gmail.com'), 
(488,'mit', 'mit@gmail.com'), 
(254, 'vic','vic@gmail.com'), 
(438, 'kenta','kenta@gmail'),
(744, 'ming', 'ming@gmail.com'),
(561, 'jan', 'jan@gmail'),
(371, 'mona', 'mona@gmail.com'),
(261,'john', 'john@gmail')
""";
select = """SELECT * from users"""
query = """SELECT * from ledger where receiver_id = 920"""
x.run_query(query)
x.search(query, True)
print(x.search(query, True))
```

3. Proof of work

<img width="1440" alt="Screenshot 2024-02-19 at 22 15 11" src="https://github.com/Rokyyz/Unit3/assets/134658259/351a2c81-5845-4f19-b9c6-9b267d77273b">
