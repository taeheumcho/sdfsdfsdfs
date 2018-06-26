import requests

url = "https://api-beta.upbit.com/v1/ticker"

querystring = {"markets":"markets"}

response = requests.request("GET", url, params=querystring)

print(response.text)