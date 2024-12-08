import requests
import Important


api_key = Important.get_api_key()
url = Important.get_url()

request = requests.get(url)
content = request.text

print(content)