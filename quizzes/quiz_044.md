# Quiz044



# 1. UML Diagram


![CommSci 33](https://github.com/Rokyyz/Unit3/assets/134658259/20b501b9-75cb-4227-87a4-723180f26c12)


# 2. solutions

What is the name of the customer and the problem that resulted in the bankruptcy of the bank?

The problem resulting in the bankruptcy of the bank is related to incorrect balances listed on the bank records for certain clients. The actual balances were supposed to be different from what was recorded, leading to discrepancies that likely contributed to financial mismanagement and ultimately bankruptcy.

Here's how you can answer the question:

Client 12: The recorded balance was 4600, but it was supposed to be 5000.
Client 13: The recorded balance was 2200, but it was supposed to be 1400.
Client 15: The recorded balance was 2300, but it was supposed to be 1500.
Client 17: The recorded balance was 2400, but it was supposed to be 1600.
Client 19: The recorded balance was 2500, but it was supposed to be 1700.

The problem seems to stem from discrepancies between the recorded balances and the actual balances. This type of error could lead to financial instability and ultimately contribute to the bankruptcy of the bank.

```.py

SELECT *                                                                                                                                                                                                                                                  
from (select accounts.account_id,                                                                                                                                                                                                                         
             accounts.balance,                                                                                                                                                                                                                            
             sum(CASE WHEN transaction_type = 'withdraw' THEN amount ELSE 0 END) AS withdraw,                                                                                                                                                             
             sum(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END)  AS deposit,                                                                                                                                                              
             sum(case when transaction_type = 'deposit' then amount else 0 end) -                                                                                                                                                                         
             sum(case when transaction_type = 'withdraw' then amount else 0 end) as real_balance,                                                                                                                                                         
             CASE                                                                                                                                                                                                                                         
                 WHEN sum(case when transaction_type = 'deposit' then amount else 0 end) -                                                                                                                                                                
                      sum(case when transaction_type = 'withdraw' then amount else 0 end) != balance THEN 'wrong'                                                                                                                                         
                 ELSE 'clear' END                                                AS 'judge'                                                                                                                                                               
                                                                                                                                                                                                                                                          
      FROM transactions                                                                                                                                                                                                                                   
               inner join                                                                                                                                                                                                                                 
           accounts on transactions.account_id = accounts.account_id                                                                                                                                                                                      
      GROUP BY accounts.account_id, accounts.balance                                                                                                                                                                                                      
                                                                                                                                                                                                                                                          
) as subquery                                                                                                                                                                                                                                             
where                                                                                                                                                                                                                                                     
    judge = 'wrong';                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                          
select customers.first_name, customers.last_name, accounts.account_id                                                                                                                                                                                     
from customers                                                                                                                                                                                                                                            
JOIN accounts                                                                                                                                                                                                                                             
on customers.customer_id = accounts.account_id                                                                                                                                                                                                            
where accounts.account_id in (12, 13, 15, 17, 19);                                                                                                                                                                                                        
```


# 3. proof of work
<img width="948" alt="Screenshot 2024-02-18 at 17 59 08" src="https://github.com/Rokyyz/Unit3/assets/134658259/c03a86e3-b50c-40f5-ad0c-6166ff82c267">
<img width="555" alt="Screenshot 2024-02-18 at 17 59 19" src="https://github.com/Rokyyz/Unit3/assets/134658259/4b6e39c6-bc30-4ff7-8fbd-140457362a6d">

