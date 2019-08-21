import requests

if __name__ == '__main__':
    payload = {'name': 'Emily', 'age': 35}
    r = requests.post("http://httpbin.org/post", data=payload)
    print(r.text)
