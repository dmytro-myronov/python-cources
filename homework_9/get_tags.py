import re

def get_all_tags(text):
    l = re.findall("#[A-Za-z0-9._%+-]*",text)
    return l



print(get_all_tags("Enter the text:#tag1,#tag2,#tag3,#newfilm: "))