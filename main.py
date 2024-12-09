import requests
import Important
import send_email


api_key = Important.get_api_key()
url = Important.get_url("tesla") #apple,tesla,techcrunch

request = requests.get(url)

#converting the data to dictionary
content = request.json()

#getting the details
news ="""\
subject: Here is today's news
"""

for article in content["articles"][:20]:
    text = f"title : {article["title"]}\ndescription: {article["description"]} \nread more: {article["url"]} \n\n"
    news = news+text

#used when getting ascii error
news = news.encode("utf-8")

receiver =Important.get_mail()
send_email.send_mail(receiver,news)