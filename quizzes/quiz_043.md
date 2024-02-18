# Quiz043


# 1. solutions


```.sqlite
SELECT COUNT(*) AS table_count
FROM sqlite_master
WHERE type='table';

select count(*) as friendly_male_count from INHABITANT where state = 'Friendly' and gender = 'Male';


select avg(gold), count(*), V.name from INHABITANT join VILLAGE V
    on V.villageid = INHABITANT.villageid group by v.name;

select count(*) as item_count from ITEM where item like 'a%';

select count(distinct job) as unique_job_count from INHABITANT;

select I.item from INHABITANT join ITEM I
    on I.owner = INHABITANT.personid group by I.item;
```


# 3. proof of work
1. <img width="1440" alt="Screenshot 2024-02-18 at 15 23 54" src="https://github.com/Rokyyz/Unit3/assets/134658259/cbc9cdf2-f21a-4664-a090-881b59e8eec9">

2. <img width="1440" alt="Screenshot 2024-02-18 at 15 24 09" src="https://github.com/Rokyyz/Unit3/assets/134658259/aefabd53-8e65-4ecc-96fc-23dffd036ede">

3. <img width="1440" alt="Screenshot 2024-02-18 at 15 24 27" src="https://github.com/Rokyyz/Unit3/assets/134658259/ee55f1cf-de5c-47d5-95cd-691ba0c50c47">

4. <img width="1440" alt="Screenshot 2024-02-18 at 15 24 43" src="https://github.com/Rokyyz/Unit3/assets/134658259/ec540196-ecdc-42e1-82d4-4adc79c3948a">

5. <img width="1440" alt="Screenshot 2024-02-18 at 15 24 54" src="https://github.com/Rokyyz/Unit3/assets/134658259/32272eea-88f8-47f4-a6b1-f43433ad59bc">

6. <img width="1440" alt="Screenshot 2024-02-18 at 15 25 13" src="https://github.com/Rokyyz/Unit3/assets/134658259/3fac550e-f33f-4e01-b3ab-77bf630c0579">
