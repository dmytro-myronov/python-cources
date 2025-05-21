from datetime import datetime, timedelta
from typing import List, Dict, Any

import get_db


def get_order_for_the_last_month() -> List[Dict[str, Any]]:
    """
    Возвращает список заказов за последний месяц, ориентируясь на переданные месяц и год.
    На данный момент игнорирует month и year и берёт заказы за последние 30 дней от текущей даты.

    :param month: Месяц (не используется в текущей реализации)
    :param year: Год (не используется в текущей реализации)
    :return: Список заказов (каждый заказ — словарь)
    """
    db, client = get_db.get_db()
    orders = db['orders']

    thirty_days_ago = datetime.now() - timedelta(days=30)
    recent_orders = list(orders.find({"order_date": {"$gte": thirty_days_ago}}))

    client.close()
    return recent_orders
