import requests
import Important


api_key = Important.get_api_key()
url = Important.get_url()

request = requests.get(url)

#converting the data to dictionary
content = request.json()

#getting the details

for article in content["articles"]:
    print(f"title : {article["title"]}\ndescription: {article["description"]} \n-------------------------------------")