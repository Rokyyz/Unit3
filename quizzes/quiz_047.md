# Quiz047

# 1. ER Diagram

![CommSci 31](https://github.com/Rokyyz/Unit3/assets/134658259/b6d6f0d3-decd-435a-9ce6-d5344929e933)

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
    if valid is True:
        print(f'Tx {split_id}, Signature matches')
    else:
        print(f"Tx {split_id}, Error signature")

my_db.close()

```
# 2. proof of work

<img width="1440" alt="Screenshot 2024-02-18 at 20 04 35" src="https://github.com/Rokyyz/Unit3/assets/134658259/4b494e91-ac94-4750-83b0-3044aa128df7">

