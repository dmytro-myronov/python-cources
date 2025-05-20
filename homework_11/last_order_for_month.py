from datetime import datetime, timedelta
import get_db


def get_order_for_the_last_month(month, year):
    # 2. READ - замовлення за останні 30 днів
    db,client = get_db.get_db()
    orders  = db['orders']
    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_orders = list(orders.find({"order_date": {"$gte": thirty_days_ago}}))
    client.close()
    return recent_orders

