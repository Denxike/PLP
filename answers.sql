

-- Question 1:
SELECT
    paymentDate,
    SUM(amount) AS total_amount
FROM
    payments
GROUP BY
    paymentDate
ORDER BY
    paymentDate DESC
LIMIT 5;

-- Question 2: 
SELECT
    customerName,
    country,
    AVG(creditLimit) AS average_credit_limit
FROM
    customers
GROUP BY
    customerName, country;

-- Question 3: 
SELECT
    productCode,
    quantityOrdered,
    (quantityOrdered * priceEach) AS total_price
FROM
    orderdetails
GROUP BY
    productCode, quantityOrdered, priceEach -- Including priceEach in GROUP BY as it affects total_price; alternatively, one could group only by productCode and quantityOrdered if priceEach is consistent for a given productCode/quantity combination, but following the prompt strictly includes grouping by the columns displayed. A more common request might aggregate by productCode alone. Let's stick to the explicit grouping requested.
ORDER BY
    productCode, quantityOrdered; -- Added ORDER BY for better readability


-- Question 4: 
SELECT
    checkNumber,
    MAX(amount) AS highest_payment_amount
FROM
    payments
GROUP BY
    checkNumber;
