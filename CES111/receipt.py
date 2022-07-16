import requests
import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime


def main():

    try:
        PRODUCT_INDEX = 0 # Index of the Product number column in the products.csv file.
        # PRODUCT_NAME = 2 # Index of the Products name column in the products_dict dictionary valu.

        response_product = requests.get('https://sergeherman.github.io/CES111/products_data_source.csv')
        with open('products.csv', 'wb') as f:
            f.write(response_product.content)
        
        product_file_name = r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\FinalProject\sergeherman.github.io\CES111\products.csv"
        # products_dict = read_dict(r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\FinalProject\sergeherman.github.io\CES111\products.csv", PRODUCT_INDEX)
        products_dict = read_dict(product_file_name, PRODUCT_INDEX)
        # products_dict = read_dict(r"products.csv", PRODUCT_INDEX)
        print(f"All Products")
        print(f'{products_dict}')
        
        request_list_file_name = r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\10\10_ProveMilestone\request.csv"
        # request_list= read_compound_list(r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\10\10_ProveMilestone\request.csv")
        request_list= read_compound_list(request_list_file_name)
        # request_list= read_compound_list(r"request.csv")
        # print(f'{request_list}')

        # These are the indexes of the elements in the request_list.
        PRODUCT_INDEX = 0
        PRODUCT_QUANTITY = 1

        # These are the indexes of the elements in the request_list.
        PRODUCT_NAME = 1
        PRODUCT_PRICE = 2

        print(f"Inkom Emporium")
        print()

        subtotal = 0
        number_of_items = 0
        # Contains a loop that reads and processes each row from the request.csv file.
        for product in request_list:

            # Retrieve from the list.
            product_index =  product[PRODUCT_INDEX]
            product_quantity = product[PRODUCT_QUANTITY]

            # Retrieve from the products_dict.
            product_data = products_dict[product_index]
            product_name = product_data[PRODUCT_NAME]
            product_price = product_data[PRODUCT_PRICE]
            subtotal += float(product_price) * float(product_quantity)
            number_of_items += int(product_quantity)

            
            print(f"{product_name}: {product_quantity} @ {product_price}")
        
        
        sales_tax = subtotal*0.06
        total = subtotal + sales_tax
        print()
        print(f"Number of Items: {number_of_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print(f"Thank you for shopping at the Inkom Emporium.")

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        # Print the current day of the week and the current time.
        print(f"{current_date_and_time:%c}")
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        print(f"missing file [Errno 2] No such file or directory: 'products.csv'")
    except PermissionError as perm_err:
        print(f"Error: Your account does not have permission to read 'products.csv'")
        print(perm_err)
    except KeyError as key_err:
        print(f'Error: unknown product ID in the request.csv file ')
        print(type(key_err).__name__, key_err)
        

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open a file named filename and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)
        
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

def read_compound_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list. Each element in the
    compound list will be a small list that contains
    the values from one row of the CSV file.

    Parameter filename: the name of the CSV file to read
    Return: a list of lists that contain strings
    """
    # Create an empty list that will
    # store the data from the CSV file.
    compound_list = []

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data about a dental office,
        # so this statement skips the first row of the
        # CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:


            # If the current row is not blank,
            # append it to the compound_list.
            if len(row_list) != 0:

                # Append one row from the CSV
                # file to the compound list.
                compound_list.append(row_list)

    # Return the compound list.
    return compound_list


# Call main to start this program.
if __name__ == "__main__":
    main()

