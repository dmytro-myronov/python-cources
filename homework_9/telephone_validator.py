import re


r = re.match(r'\(\d{3}\) \d{3}-\d{4}',"(123) 456-7890")
print(bool(r))

r = re.match(r'\d{3}-\d{3}-\d{4}',"123-456-7890")
print(bool(r))

r = re.match(r'\d{3}.\d{3}.\d{4}',"123.456.7890")
print(bool(r))

r = re.match(r'^[0-9]*$',"1234567890")
print(bool(r))