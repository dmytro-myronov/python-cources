def format_date(date_str: str) -> str:
    """
    Converts a date string from the format 'DD/MM/YYYY' to 'YYYY-MM-DD'.

    Args:
        date_str (str): A date string in the format 'DD/MM/YYYY'.

    Returns:
        str: The formatted date string in the format 'YYYY-MM-DD'.
    """
    day, month, year = date_str.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"


print(format_date("20/05/2025"))
