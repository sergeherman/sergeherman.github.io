import requests

# payload = {'username': 'corey', 'password': 'testing'}
# response = requests.get('https://sergeherman.github.io/CES111/test_data.md')
# response = requests.get('https://sergeherman.github.io/CES111/products.csv')

product_file_name = r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\FinalProject\sergeherman.github.io\CES111\products.csv"
response_product = requests.get('https://sergeherman.github.io/CES111/products_data_source.csv')
with open(product_file_name, 'wb') as f:
    f.write(response_product.content)

# print(response_product.text) 
# response = requests.get('https://httpbin.org/get', params=payload)
# response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Wooden_boomerang_asv2021-05.jpg/750px-Wooden_boomerang_asv2021-05.jpg')
# response = requests.post('https://httpbin.org/post', data=payload)
# r_dict = response.json()
# print(r_dict['form'])
# # print(help(r))
# print(response.text) 
# print(response.json()) 
# print(response.content)
# print(response.url)
# print(response.status_code)
# print(response.ok)
# print(response.headers)
# print(response.text)

# with open('test_picture.jpg', 'wb') as f:
#     f.write(response.content)
# url = 'https://www.youtube.com/results'
# query = {'search_query': 'audy'}
# response = requests.get(url)

# response = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
# print(response) 
