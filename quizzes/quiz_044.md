# Quiz044



# 1. UML Diagram




# 2. solutions


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

