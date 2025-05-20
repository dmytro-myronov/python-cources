from datetime import datetime

import get_db

db,client = get_db.get_db()

products = db['products']
orders = db['orders']

# 1. CREATE - додати продукти
products.insert_many([
    {"name": "Телефон", "price": 10000, "category": "Електроніка", "stock": 50},
    {"name": "Ноутбук", "price": 25000, "category": "Електроніка", "stock": 30}
])

# CREATE - додати замовлення
orders.insert_one({
    "order_number": 1,
    "client": "Іван Іванов",
    "products": [
        {"product_name": "Телефон", "quantity": 2},
        {"product_name": "Ноутбук", "quantity": 1}
    ],
    "total_amount": 45000,
    "order_date": datetime.now()
})
client.close()