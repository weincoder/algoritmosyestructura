# []{}
import requests
import bs4
url = "https://www.eltiempo.com"

response = requests.get(url)

print (dir(response))