import re

text = "Contact us at abc@gmail.com or xyz123@yahoo.com"

emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

print("Email addresses found:")
print(emails)
