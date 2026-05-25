import re

text = "Hello bhai, Python seekh rahe ho"
pattern = "Hello"

result = re.match(pattern, text)

if result:
    print("Matched at beginning")
else:
    print("No match at beginning")