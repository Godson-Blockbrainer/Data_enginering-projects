--------------------------------------------------------------------------------------------------------
-- Project 1 -- Provide insights and data to help a marketing team implement a Customer Loyalty program.

-- Question 1 -- Provide the top 10 customers (full name) by revenue, the country they shipped to, the cities and 
-- their revenue (orderqty * unitprice).
-- This insight will help you understand where your top spending customers are coming from. You can 
-- market better, get more capable customer service rep, have more stock and build partnerships in these
-- countries and cities.



/* customer , fullname , revenue ,country ,cities and there revenue(orderqty * unitprice)
Table needed-- 
FirstName----SalesLT.Customer-----C
LastName-----SalesLT.Customer------C
Country -----SalesLT.Address ---A
city-----SalesLT.Address ----A
orderqty----SalesLT.SalesOrderDetail------SO
unitprice------SalesLT.SalesOrderDetail------SO
UniqueKey ---- C & CA -----CustomerID
Table -SalesLT.SalesrOrderHeader SOH  becuse there is a relationship with SalesLT.Customer  which is CustomerID
Table- SalesLT.Customer Address -- Beause there is a relationship to SalesLT.Address whichc is AddressID column
UniqueKey ----  SO & SOH ----- & SalesOrderID

*/
Select Top(10) Concat(C.FirstName,'', C.LastName) AS Fullname , A.CountryRegion, A.City , SUM(SO.orderqty * SO.unitprice) As revenue 
from SalesLT.Customer C join SalesLT.SalesOrderHeader SOH on C.CustomerID = SOH.CustomerID 
join SalesLT.CustomerAddress CA on CA.CustomerID = C.CustomerID
Join SalesLT.Address A on A.AddressID = CA.AddressID
Join SalesLT.SalesOrderDetail SO on SO.SalesOrderID = SOH.SalesOrderID Group by C.FirstName, C.LastName, A.CountryRegion, A.city order by revenue desc

/*--------------------------------------------------------------------------------------------------------
-- Question 2 -- Create 4 distinct Customer segments using the total Revenue (orderqty * unitprice) by customer. 
-- List the customer details (ID, Company Name), Revenue and the segment the customer belongs to. 
-- This analysis can use to create a loyalty program, mmarket customers with discount or leave customers as-is.

CustomerID----SalesLT.Customer -- C 
CompanyName-----SalesLT.Customer ---C
orderqty----SalesLT.SalesOrderDetail---SO
unitprice----SalesLT.SalesOrderDetail---SO 
relationship - CustomerID, SalesOrderID

*/
Select C.CustomerID, C.CompanyName,  SUM(SO.orderqty * SO.unitprice) As revenue, CASE
        WHEN SUM(SO.orderqty * SO.unitprice) >= 100000 THEN 'High Revenue'
        WHEN SUM(SO.orderqty * SO.unitprice) >= 50000 THEN 'Medium Revenue'
        WHEN SUM(SO.orderqty * SO.unitprice) >= 10000 THEN 'Low Revenue'
        ELSE 'Minimal Revenue'
    END AS CustomerSegments  from SalesLT.Customer C 
join SalesLT.SalesOrderHeader SOH on SOH.CustomerID = C.CustomerID
join SalesLT.SalesOrderDetail SO on SO.SalesOrderID = SOH.SalesOrderID 
GROUP BY
    C.CustomerID,
    C.CompanyName
ORDER BY
    Revenue DESC;


/*-------------------------------------------------------------------------------------------------------
-- Question 3 -- What products with their respective categories did our customers buy on our last day of business?
-- List the CustomerID, Product ID, Product Name, Category Name and Order Date.
-- This insight will help understand the latest products and categories that your customers bought from. This will help
-- you do near-real-time marketing and stockpiling for these products.


CustomerID----SalesLT.Customer--- C 
ProductID----SalesLT.Product---- P 
CategoryName ---SalesLT.ProductCategory ----PC
OrderDate ---SalesLT.SalesOrderHeader-- SOH
relationship - ProductID, SalesOrderID, ProductCategoryID
*/
Select C.CustomerID, P.ProductID, PC.Name as CategoryName, SOH.OrderDate from SalesLT.Product P
join SalesLT.SalesOrderDetail SO on SO.ProductID = P.ProductID
join SalesLT.SalesOrderHeader SOH on SOH.SalesOrderID = SO.SalesOrderID
join  SalesLT.ProductCategory PC on PC.ProductCategoryID = P.ProductCategoryID
join SalesLT.Customer C on C.CustomerID = SOH.CustomerID


/*
----------------------------------------------------------------------------------------------------------------
-- Question 4 -- Create a View called customersegment that stores the details (id, name, revenue) for customers
-- and their segment? i.e. build a view for Question 2.
-- You can connect this view to Tableau and get insights without needing to write the same query every time.
*/

Create VIEW customersegment AS  Select C.CustomerID, C.CompanyName,  SUM(SO.orderqty * SO.unitprice) As revenue, CASE
        WHEN SUM(SO.orderqty * SO.unitprice) >= 100000 THEN 'High Revenue'
        WHEN SUM(SO.orderqty * SO.unitprice) >= 50000 THEN 'Medium Revenue'
        WHEN SUM(SO.orderqty * SO.unitprice) >= 10000 THEN 'Low Revenue'
        ELSE 'Minimal Revenue'
    END AS CustomerSegments  from SalesLT.Customer C 
join SalesLT.SalesOrderHeader SOH on SOH.CustomerID = C.CustomerID
join SalesLT.SalesOrderDetail SO on SO.SalesOrderID = SOH.SalesOrderID 
GROUP BY
    C.CustomerID,
    C.CompanyName

Select * from customersegment --- proves that the view has been created 

-----------------------------------------------------------------------------------------------------------------
/*-- Question 5 -- What are the top 3 selling product (include productname) in each category (include categoryname)
-- by revenue? Tip: Use ranknum
-- This analysis will ensure you can keep track of your top selling products in each category. The output is very
-- powerful because you don't have to write multiple queries to be able to see your top selling products in each category.
-- This analysis will inform your marketing, your supply chain, your partnerships, position of products on your website, etc.
-- NB: This question is asked a lot in interviews!

-----------------------------------------------------------------------------------------------------------------

ProductID----SalesLT.Product---- P 
ProductName--SalesLT.Product----P
orderqty----SalesLT.SalesOrderDetail---SO
unitprice----SalesLT.SalesOrderDetail---SO
CategoryName ---SalesLT.ProductCategory ----PC
relationship - ProductID, SalesOrderID, ProductCategoryID

*/

select P.ProductID, P.Name as ProductName, PC.Name AS ProductCategory,  SUM(SO.orderqty * SO.unitprice) As revenue ,
  RANK() OVER (PARTITION BY PC.Name ORDER BY SUM(SO.orderqty * SO.unitprice) DESC) AS RankNum
from SalesLT.Product P 
join  SalesLT.SalesOrderDetail SO on SO.ProductID = P.ProductID
join SalesLT.ProductCategory PC on PC.ProductCategoryID = P.ProductCategoryID 
Group by  P.ProductID, P.Name ,PC.Name Order by revenue ,RankNum

