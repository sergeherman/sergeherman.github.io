import requests
import csv
from datetime import datetime
import yaml # data serialization format designed for human readability 


def main():

    try:
        CUSTOMER_INDEX = 0 # Index of the Customer number column in the customers.csv file.
        # CUSTOMER_NAME = 2 # Index of the Customers name column in the customers_dict dictionary valu.

        # read customer data from an internet site and write it in to the working file of the application for further manipulations
        customer_file_name = r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\FinalProject\sergeherman.github.io\CES111\customers.csv"
        
        def add_customer():
            """ Read customers data from an internet site and write it in 
            to the working file of the application for further manipulations """
            response_customer = requests.get('https://sergeherman.github.io/CES111/customers_data_source.csv')
            with open(customer_file_name, 'wb') as f:
                f.write(response_customer.content)
        
        # call the add_customer() function
        add_customer()
        
        # customers_dict = read_dict(r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\FinalProject\sergeherman.github.io\CES111\customers.csv", CUSTOMER_INDEX)
        customers_dict = read_dict(customer_file_name, CUSTOMER_INDEX)
        # customers_dict = read_dict(r"customers.csv", CUSTOMER_INDEX)
        print()
        print(f"CUSTOMERS ORDERS TRACKING TOOL")
        print()
        print(f"All Customers Info: Customer #, Customer Name, Package Size Defined for this Customer:")
        print()
        # print(f'{customers_dict}')
        print(yaml.dump(customers_dict, default_flow_style=False))
        
        request_file_name = r"C:\Users\hermansp\Documents\EDU\BYU_Pathway\BYUI\2022Spring\CES111\FinalProject\sergeherman.github.io\CES111\request.csv"
        
        def add_order():
            """ Read requests data from an internet site and write it in 
            to the working file of the application for further manipulations """
            
            response_request = requests.get('https://sergeherman.github.io/CES111/request_data_source.csv')
            with open(request_file_name, 'wb') as f:
                f.write(response_request.content)
            
        # call the add_order() function
        add_order()    
       
        request_list= read_compound_list(request_file_name)
        # request_list= read_compound_list(r"request.csv")
        # print(f'{request_list}')

        # These are the indexes of the elements in the request_list.
        CUSTOMER_INDEX = 0
        CUSTOMER_QUANTITY = 1

        # These are the indexes of the elements in the request_list.
        CUSTOMER_NAME = 1
        CUSTOMER_PRICE = 2

        print(f"Customers Orders Statistics")
        print()
        print(f"Customer Name: Order Quantity & Package Size (items per package):")
        

        subtotal = 0
        number_of_items = 0
        
        # Contains a loop that reads and processes each row from the request.csv file.
        for customer in request_list:

            # Retrieve from the list.
            customer_index =  customer[CUSTOMER_INDEX]
            customer_quantity = customer[CUSTOMER_QUANTITY]

            # Retrieve from the customers_dict.
            customer_data = customers_dict[customer_index]
            customer_name = customer_data[CUSTOMER_NAME]
            customer_price = customer_data[CUSTOMER_PRICE]
            subtotal += float(customer_price) * float(customer_quantity)
            number_of_items += int(customer_quantity)

            
            print(f"{customer_name}: {customer_quantity} @ {customer_price}")
        
        number_of_orders = len(request_list)
        ave_number_of_items_per_order = subtotal / number_of_orders
        
        print()
        print(f"Number of Orders: {number_of_orders}")
        print(f"Number of Ordered Packages: {number_of_items}")
        print(f"Total Number of Ordered Items: {subtotal}")
        print(f"Average Number of Ordered Items per Order: {ave_number_of_items_per_order}")
        print()
        print(f"Thank you for using the Customer Order Tracking Tool.")

        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()

        # Print the current day of the week and the current time.
        print(f"{current_date_and_time:%c}")
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        print(f"missing file [Errno 2] No such file or directory: 'customers.csv'")
    except PermissionError as perm_err:
        print(f"Error: Your account does not have permission to read 'customers.csv'")
        print(perm_err)
    except KeyError as key_err:
        print(f'Error: unknown customer ID in the request.csv file ')
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

