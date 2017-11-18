import requests
boom = requests.get('ftp://ftp.engineer.bmstu.ru/CiscoVPNClient.zip')
print(boom.text)
print(boom.status_code)
print(boom.json())