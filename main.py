import json
import requests
import telebot
import time

TOKEN = "5651594004:AAHGmicPOInrM3FbhtKqMBhDvoAwNKbtMCo"
CHAT_ID_USERBOT = '@cityexpet_wg'
URL = 'https://cityexpert.rs/api/Search?req=%7B%22ptId%22%3A%5B5%2C2%2C1%5D%2C%22cityId%22%3A1%2C%22rentOrSale%22%3A%22r%22%2C%22minPrice%22%3A200%2C%22maxPrice%22%3A1000%2C%22searchSource%22%3A%22regular%22%2C%22sort%22%3A%22datedsc%22%7D'
bot = telebot.TeleBot(TOKEN)

req = requests.get(URL)
request_data = json.loads(req.text)

db = open('db.txt')
tmp_arr_int = []
tmp_arr_str = []
for line in db:
    if line not in '\n':
        tmp_arr_str.append(line)
        tmp_arr_int.append(int(line))
db.close()
db = open('db.txt', 'w')

for i in request_data['result']:
    time.sleep(30)
    if i['propId'] not in tmp_arr_int:
        db.write(str(i['propId']) + '\n')
        bot.send_message(CHAT_ID_USERBOT,
                         'https://cityexpert.rs/en/properties-for-rent/belgrade/' + str(i['propId']) + '/wg')

for t in tmp_arr_str:
    db.write(t)
db.close()

