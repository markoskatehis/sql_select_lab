import sqlite3
import pandas as pd

conn = None
conn = sqlite3.connect("data.sqlite")

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)

df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)

df_alias = pd.read_sql("""
SELECT employeeNumber AS ID, lastName
FROM employees
""", conn)

df_executive = pd.read_sql("""
SELECT
    employeeNumber,
    lastName,
    jobTitle,
    CASE
        WHEN jobTitle = 'President'
          OR jobTitle = 'VP Sales'
          OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)

df_name_length = pd.read_sql("""
SELECT
    LENGTH(lastName) AS name_length
FROM employees
""", conn)

df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)

sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered, 0)) AS total_price
FROM orderDetails
""", conn)["total_price"]

df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    STRFTIME('%d', orderDate) AS day,
    STRFTIME('%m', orderDate) AS month,
    STRFTIME('%Y', orderDate) AS year
FROM orders
""", conn)