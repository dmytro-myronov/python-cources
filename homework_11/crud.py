import get_db
from datetime import datetime, timedelta

db,client = get_db.get_db()
products = db['products']
orders = db['orders']


# 3. UPDATE - оновити кількість продукту після покупки
products.update_one(
    {"name": "Телефон"},
    {"$inc": {"stock": -2}}
)

# 4. DELETE - видалити продукти, яких немає в наявності
products.delete_many({"stock": {"$lte": 0}})
thirty_days_ago = datetime.now() - timedelta(days=30)
# 5. Агрегація - загальна кількість проданих продуктів за період
sold_products_count = orders.aggregate([
    {"$match": {"order_date": {"$gte": thirty_days_ago}}},
    {"$unwind": "$products"},
    {"$group": {
        "_id": "$products.product_name",
        "total_quantity": {"$sum": "$products.quantity"}
    }}
])
print("Кількість проданих продуктів за 30 днів:")
for product in sold_products_count:
    print(product)

# 6. Агрегація - загальна сума всіх замовлень клієнта
client_total = orders.aggregate([
    {"$match": {"client": "Іван Іванов"}},
    {"$group": {"_id": "$client", "total_sum": {"$sum": "$total_amount"}}}
])
print("Загальна сума замовлень клієнта Іван Іванов:")
for total in client_total:
    print(total)

# 7. Індекси для поля category
products.create_index("category")

client.close()