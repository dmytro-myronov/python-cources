def format_date(date_str) ->str:
    # Розбиваємо дату по символу "/"
    day, month, year = date_str.split('/')
    # Формуємо новий формат
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

# Приклад використання:
print(format_date("20/05/2025"))  # Виведе: 2025-05-20
