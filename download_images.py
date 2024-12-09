from os import write

import requests


def create_image(url, name, end_notation):

    request = requests.get(url)

    with open(fr"images\{name}.{end_notation}", "wb") as file:
        file.write(request.content)

create_image("https://i.pinimg.com/550x/a8/47/9a/a8479a922b151b03df56a6db105dc5dd.jpg","animePFP","jpg")