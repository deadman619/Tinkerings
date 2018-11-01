import mysql.connector
import random

#Connect to database
try:
    conn = mysql.connector.Connect(host='localhost', user='root', password='', db='test')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Wrong username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

#Get cursor, allows to edit DB
cursor = conn.cursor()                                                                           

#conn.commit() Commit, i.e. save changes
#Tables need to get dropped in reverse order because of key dependancies or cursor.execute('SET FOREIGN_KEY_CHECKS=0'))
#But you need to set it back to 1 after table dump

cursor.execute("DROP TABLE if exists products_returned")
cursor.execute("DROP TABLE if exists return_reasons")
cursor.execute("DROP TABLE if exists returns")
cursor.execute("DROP TABLE if exists products_ordered")
cursor.execute("DROP TABLE if exists orders")
cursor.execute("DROP TABLE if exists products")
cursor.execute("DROP TABLE if exists customers")

                                                                               

cursor.execute('''
                CREATE TABLE customers(id INT PRIMARY KEY AUTO_INCREMENT,
                name TEXT,
                address TEXT,
                zipcode TEXT,
                city TEXT)''')

cursor.execute('''
                CREATE TABLE products(id INT PRIMARY KEY AUTO_INCREMENT,
                name TEXT,
                size TEXT)''')

cursor.execute('''
                CREATE TABLE orders(id INT PRIMARY KEY AUTO_INCREMENT,
                date DATE,
                customer_id INT,
                FOREIGN KEY(customer_id) REFERENCES customers(id))''')

cursor.execute('''
                CREATE TABLE products_ordered(id INT PRIMARY KEY AUTO_INCREMENT,
                order_id INT,
                product_id INT,
                FOREIGN KEY(order_id) REFERENCES orders(id),
                FOREIGN KEY(product_id) REFERENCES products(id))''')

cursor.execute('''
                CREATE TABLE returns(id INT PRIMARY KEY AUTO_INCREMENT,
                order_id INT UNIQUE,
                FOREIGN KEY(order_id) REFERENCES orders(id))''')

cursor.execute('''
                CREATE TABLE return_reasons(id INT PRIMARY KEY AUTO_INCREMENT,
                reason TEXT)''')

cursor.execute('''
                CREATE TABLE products_returned(id INT PRIMARY KEY AUTO_INCREMENT,
                returns_id INT,
                return_reasons_id INT,
                products_ordered_id INT,
                FOREIGN KEY(returns_id) REFERENCES returns(id),
                FOREIGN KEY(return_reasons_id) REFERENCES return_reasons(id),
                FOREIGN KEY(products_ordered_id) REFERENCES products_ordered(id))''')


#Populate database with RNG
for i in range(50):
    rarity = random.choice(['Grey', 'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary'])
    prefix = random.choice(["Champion's", "Vanquisher's", "Warrior's", "Conqueror's", "Gladiator's", "Veteran's", "Arena Master's"])
    item = random.choice(['Spaulders', 'Staff', 'Cloak', 'Helmet', 'Dagger', 'Zweihander', 'Severed Head'])
    name = '%s %s %s' %(rarity, prefix, item)
    sizes = random.choice (['Big', 'Gigantic', 'Massive', 'Giant'])
    cursor.execute('INSERT INTO products(name, size) VALUES(%s, %s)', (name, sizes))

for i in range(25):
    name = random.choice(['Garrosh', 'Thrall', 'Sylvanas', 'Genn', 'Varian', 'Arthas', 'Gul\'dan', 'Anduin', 'Sargeras'])
    address = "3:16 Gimmick Street"
    zipcode = random.randint(10000,99999)
    city = random.choice(["Orgrimmar", "Stormwind", "Dalaran", "Ironforge", "Zandalar", "Shattrath", "Darnassus", "The Crossroads"])
    cursor.execute('INSERT INTO customers(name, address, zipcode, city) VALUES(%s, %s, %s, %s)', (name, address, zipcode, city))
    date = "2020-12-01"
    customer_id = cursor.lastrowid
    cursor.execute('INSERT INTO orders(date, customer_id) VALUES (%s, %s)', (date, customer_id))
    cursor.execute('SELECT id FROM products')
    all_products_ids = cursor.fetchall()
    all_products_ids = [x for (x,) in all_products_ids]
    product = random.choice(all_products_ids)
    cursor.execute('INSERT INTO products_ordered(order_id, product_id) VALUES (%s, %s)', (customer_id, product))
    order_id = cursor.lastrowid
    if order_id % 3 == 0:
        cursor.execute('INSERT INTO returns(order_id) VALUES (%s)', (order_id,))
        returns_id = cursor.lastrowid
        reason = random.choice(["bad", "broken", "overpriced", "too low-level"])
        cursor.execute('INSERT INTO return_reasons(reason) VALUES("The item was %s")', (reason,))
        return_reasons_id = cursor.lastrowid
        cursor.execute('INSERT INTO products_returned(returns_id, return_reasons_id, products_ordered_id) VALUES (%s, %s, %s)', (returns_id, return_reasons_id, order_id))


conn.commit()

#Test query

print ('Return reasons:')
cursor.execute('''SELECT products_returned.id, customers.name, products.name, return_reasons.reason FROM products_returned
                JOIN return_reasons ON return_reasons.id = products_returned.id
                JOIN products_ordered ON products_ordered.id = products_returned.id
                JOIN orders ON orders.id = products_ordered.order_id
                JOIN customers ON customers.id = orders.customer_id
                JOIN products ON products_ordered.product_id = products.id''')
for row in cursor.fetchall():
    print (row)

conn.close()
