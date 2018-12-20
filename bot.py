import os
import requests


token = os.getenv('TELE_TOKEN')
method = 'getUpdates'
# url = "https://api.telegram.org/bot{}/{}".format(token,method)
url = "https://api.hphk.io/telegram/bot{}/getUpdates".format(token)

res = requests.get(url).json()

user_id = res["result"][0]["message"]["from"]["id"]
msg = "최보균 좌절하지마라!"

method = 'sendmessage'

msg_url = "https://api.hphk.io/telegram/bot{}/{}?chat_id={}&text={}".format(token,method,user_id,msg)
requests.get(msg_url)
print(msg_url)

print(user_id)