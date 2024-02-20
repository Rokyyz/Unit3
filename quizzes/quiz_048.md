## quiz_048

# 1. ER Diagram

![CommSci 31](https://github.com/Rokyyz/Unit3/assets/134658259/b6d6f0d3-decd-435a-9ce6-d5344929e933)


# 2. Solution
```.py
import sqlite3
from passlib.hash import sha256_crypt
hasher = sha256_crypt.using(rounds=3000)


def encrypt(user_passowrd):
    return hasher.encrypt(user_passowrd)


def check(hashed_password, user_password):
    return hasher.verify(user_password, hashed_password)


class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


x = database_worker("bitcoin_exchange.db")
query = "SELECT * from ledger"
result = x.search(query)

x.close()
bitcoin_amount=0

for row in result:
    id= row[0]
    sender_id=row[1]
    receiver_id=row[2]
    amount=row[3]
    hash=row[4]
    string_hash=f"id {id},sender_id {sender_id},receiver_id {receiver_id},amount {amount}"
    equal=check(hashed_password = hash, user_password = string_hash)
    if equal is False:
        print(f"{id} Invalid transaction")
    else:
        print(f"{id} Valid transaction")
        bitcoin_amount+=amount
print(f"total transferred {bitcoin_amount} BTC")
```

# 3. Proof of work

<img width="1440" alt="Screenshot 2024-02-18 at 20 17 08" src="https://github.com/Rokyyz/Unit3/assets/134658259/5471ce41-d5e4-42cb-a1d0-750cd1ca2c88">

