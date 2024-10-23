import pymysql

# (1) DB connection
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# (2) CRUD

## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    # print("customers : ", customers)
    print("customerNumber : ", customers['customerNumber'])
    print("customerName : ", customers['customerName'])
    print("customerCountry : ", customers['country'])

    cursor.close()

## 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()
    name = 'san'
    family_name = 'kang'
    sql = f"INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) VALUES (498, 'New Customer', '{name}', '{family_name}', '123-456-7890', '123 Street', 'Suite 1', 'ULSAN', 'State', 44928, 'Country', 1002, 50000.00)"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# add_customer()

## 3. UPDATE SET
def update_customer():
    cursor = connection.cursor()
    update_name = "He is not human"
    contactLastName = "alien"

    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber=497"

    cursor.execute(sql)
    connection.commit()
    cursor.close

# update_customer()

## 4. DELETE FROM
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 497"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()