import requests
from background_task import background


@background
def push(to, content):
    data = {
        'device_id': to,
        'content': content,
    }
    try:
        requests.post('localhost:7000', json=data)
    except requests.exceptions.InvalidSchema:
        pass
