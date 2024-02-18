# Quiz047



# 1. UML Diagram




# 2. solutions
```.py
from mon_8_jan.my_lib import DatabaseWorker, check_hash

q = """ SELECT * from ledger"""

my_db = DatabaseWorker("bitcoin_exchange.db")
s = my_db.search(query=q, multiple=True)

for row in s:
    split_id = row[0]
    split_sender_id = row[1]
    split_receiver_id = row[2]
    split_amount = row[3]
    split_signature = row[4]
    text = f"id {split_id},sender_id {split_sender_id},receiver_id {split_receiver_id},amount {split_amount}"
    valid = check_hash(split_signature,text)
    print(valid)

my_db.close()
```
# 3. proof of work


