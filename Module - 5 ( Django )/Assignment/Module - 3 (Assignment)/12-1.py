import re

text = "Hello bhai, Python seekh rahe ho"
pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Word found at position:", result.start())
else:
    print("Word not found")