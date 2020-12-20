import requests

response = requests.get('https://www.reddit.com/r/investing/new.json?')

print(response.content)