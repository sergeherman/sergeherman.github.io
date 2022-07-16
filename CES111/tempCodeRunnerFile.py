response = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
# print(response) 