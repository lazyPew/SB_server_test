import requests

print('input username: ')
username = input()
print('input password: ')
password = input()


while True:
    print("what you want to say?")
    text = input()
    response = requests.post(
        'http://127.0.0.1:5000/send',
        json = {'username': username, 'password': password, 'text': text}
    )
    if response.status_code == 200:
        print("msg sent")
        print()