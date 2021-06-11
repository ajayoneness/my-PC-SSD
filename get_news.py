import requests

def article_content():
    content = dict()
    content['title'] = 'auto post'
    content['body'] = " # Set Default Status For Post .i.e Publish Default Is Draft We Are Done With This Part :) Lets Try To Run It"
    content['image'] = '1.jpg'
    return content

img=requests.get("1.jpg")
print(img)

resp = requests.get(article.top_image)
with open('1.jpg', 'wb') as imagefile:
    imagefile.write(resp.content)
    content['image'] = '1.jpg'

