import requests as req

url="https://2dommedical.com/ptp"

def rem(file):
    try:
        return req.post(url, data={'act': 'rem', 'file': file}).text
    except:
        return False
def get(file):
    try:
        return req.post(url, data={'act': 'get', 'file': file}).text
    except:
        return False
def put(file, data):
    try:
        return req.post(url, data={'act': 'put', 'file': file, 'data': str(data)}).text
    except:
        return False
def app(file, data):
    try:
        return req.post(url, data={'act': 'app', 'file': file, 'data': str(data)}).text
    except:
        return False
def rep(file, data):
    try:
        return req.post(url, data={'act': 'rep', 'file': file, 'data': str(data)}).text
    except:
        return False
angouFTP=True
