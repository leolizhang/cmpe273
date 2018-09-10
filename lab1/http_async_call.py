url = 'https://webhook.site/9a50218d-abde-4161-8f69-d9f4fb730c63'

import requests, time

def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value
async def post_url(url):
    response = requests.get(url)
    return response.headers.get('Date')
async def print_response(url, num):
    for i in range(num):
        response = await post_url(url)
        print(i + 1, response)
run(print_response(url, 3))
