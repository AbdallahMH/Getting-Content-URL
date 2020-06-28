# import the library
import requests

# we assign the object coming from the url to 'r'
r = requests.get('https://www.google.com')

# Opens a file, named test.txt (if it doesn't exist, it will create a new file with that name)
# 'wb' write bytes.
with open('test.txt', 'wb') as opened_file:
    opened_file.write(r.content)
