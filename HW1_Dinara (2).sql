/*
Dinara's HW
Task 1
Q1: Find the name and weight of each red part*/
USE Parts;
SELECT PNAME, WEIGHT
FROM PART p
WHERE p.COLOUR = 'RED';
/*Find all unique supplier(s) name from London*/
SELECT DISTINCT SNAME
FROM SUPPLIER s
WHERE s.CITY = 'LONDON';

/*TASK 2

Q1: Find out how many sales (quantity) were recorded each week, per day (where available)
This would look like:
Week 1, Tuesday, 5
Week 1, Wednesday, 2
Week 2, Monday, 1
Week 2, Friday, 8 */
USE shop;
SELECT Week, Day, COUNT(*) AS 'SalesAmount'
FROM SALES1
GROUP BY Week,Day
ORDER BY Week,Day;
/*got curious and calculated the number of sales per week*/
SELECT Week, COUNT(*) AS 'SalesAmount'
FROM SALES1
GROUP BY Week
ORDER BY Week;

/*Q2:Change the name of salesperson Inga to be Annette instead 
I kept recieving error 1175 on this action, so after googling had to disable the safe mode first*/


USE SHOP;
SET SQL_SAFE_UPDATES = 0;
UPDATE SALES1
SET SalesPerson = 'Annette'
WHERE SalesPerson = 'Inga';
SET SQL_SAFE_UPDATES = 1;

/*Q3: Find out how many sales Annette logged
Note we’re looking for quantity here - e.g. if Annette did 6 sales, then output would be 6)
Here I don't really understand the question so I did two versions 1- for the ammount of sales Annete did, 2 -for the number of sales she logged in*/
SELECT s1.SalesAmount
FROM SALES1 s1
WHERE SalesPerson = 'Annette';

SELECT COUNT(SalesAmount)
FROM SALES1
WHERE SalesPerson = 'Annette';


/*Q4: Find the total (sum) sales amount by each person by day*/
SELECT SalesPerson, Day, SUM(SalesAmount)
FROM SALES1
GROUP BY SalesPerson, Day
ORDER BY SalesPerson;

/*Q5:How much (sum) each person sold for (I added order by to highlight the largest sales amount */
SELECT SalesPerson, SUM(SalesAmount)
FROM SALES1
GROUP BY SalesPerson
ORDER BY  SUM(SalesAmount) DESC;


/*Q6: How much (sum) each person sold for, including the number of sales per person, their average, lowest and highest sale amounts*/
SELECT SalesPerson, SUM(SalesAmount), COUNT(SalesAmount), AVG(SalesAmount), MIN(SalesAmount), MAX(SalesAmount)
FROM SALES1
GROUP BY SalesPerson;


/*Q7: Find the total  (sum) monetary sales amount achieved by each store */
SELECT Store, SUM(SalesAmount)
FROM SALES1
GROUP BY Store;

/*Q8:Find the number of sales by each person if they did less than 3 sales for the past period*/
SELECT SalesPerson, COUNT(SalesAmount)
FROM SALES1
GROUP BY SalesPerson
HAVING COUNT(SalesAmount) < 3;

/*Q9:Find the total (sum) amount of sales by month where combined total is less than £100
*/
USE Shop;
SELECT Month, SUM(SalesAmount) AS Total_Sales_Amount
FROM SALES1
GROUP BY Month
HAVING SUM(SalesAmount) <100;

/*TASK3 
Q1: Return the name and city of each project that’s not supplied by a London-based supplier
*/

USE Parts;
SELECT JNAME, CITY
FROM PROJECT
WHERE J_ID IN 
(SELECT J_ID FROM SUPPLY
WHERE S_ID IN
(SELECT S_ID FROM SUPPLIER
WHERE CITY != 'London')
);

/*Q2:Return the supplier name, part name and project name for each case where not only does the supplier supply a project with a part, 
but also the supplier’s city, project city and part city are the same 
For this task I decided to use syntax with "Using" instead of "ON" for joins as the ids I use have exactly the same names*/

USE Parts;
SELECT PROJECT.JNAME AS PROJECT_JNAME,
SUPPLIER.SNAME AS SUPLLIER_SNAME, 
PART.PNAME AS PART_PNAME
FROM PROJECT 
JOIN SUPPLY USING (J_ID)
JOIN SUPPLIER USING(S_ID)
JOIN PART USING(P_ID)
WHERE  PROJECT.CITY =  SUPPLIER.CITY AND SUPPLIER.CITY = PART.CITY AND PROJECT.CITY = PART.CITY;







