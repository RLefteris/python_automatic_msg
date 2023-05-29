import requests
import time, schedule, json

def send_messg():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '+...', #phone number
        'message': 'success!',
        'key': 'textbelt'
    })
    print(resp.json())

schedule.every(20).seconds.do(send_messg)

while True:
    schedule.run_pending()
    time.sleep(1)