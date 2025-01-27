def read_and_find_substring(filename, substring):
    """
    Reads a file line by line and searches for a specified substring in each line.

    Args:
        filename (str): The path to the file to be read.
        substring (str): The substring to search for in each line.

    Yields:
        str: The line containing the substring, stripped of leading/trailing whitespace.

    Prints:
        A message indicating the index of the substring in the line if found.
    """
    with open(filename, 'r') as file:
        for line in file:
            index = line.strip().find(substring)
            if index != -1:
                print(f"Found `{substring}`")
                yield line.strip()


def add_line_to_file(lines):
    """
    Appends a list of lines to a log file called 'filter_logs.log'.

    Args:
        lines (list): A list of strings (lines) to be written to the log file.
    """
    with open('filter_logs.log', 'a') as file:
        for line in lines:
            file.write(line + '\n')


# Example usage: Find lines containing 'newsletter_send_all' in 'cron.log.3' and write them to 'filter_logs.log'
gen = read_and_find_substring('cron.log.3', 'newsletter_send_all')

# Add the lines containing the substring to the log file
add_line_to_file([text for text in gen])
