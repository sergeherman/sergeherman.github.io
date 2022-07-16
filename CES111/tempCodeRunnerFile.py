with open('products.csv', 'wb') as f:
    f.write(response_product.content)