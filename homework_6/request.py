from bs4 import BeautifulSoup
import requests


def add_line_to_file(lines: list):
    """
    Appends a list of lines to a log file called 'filter_logs.log'.

    Args:
        lines (list): A list of strings (lines) to be written to the log file.
    """
    with open('films_title.txt', 'a') as file:
        for line in lines:
            file.write(line + '\n')


try:
    request = requests.get("https://go.utorr.cc/")
    html_content = request.text
    soup = BeautifulSoup(html_content, "html.parser")

    elements = soup.find_all("div", id="dle-content")[0].find_all("div", class_="post")
    film_elements = soup.find_all("div", class_="post-title")
    films_list = []
    for film in film_elements:
        title = film.get_text(strip=True)
        films_list.append(title)
        print(title)
    add_line_to_file(films_list)

except Exception as e:
    print(f"request error {e}")
