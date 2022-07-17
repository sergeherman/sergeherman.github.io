# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

from receipt import read_dict
from os import path
from tempfile import mktemp
from pytest import approx
import pytest


def test_read_dict():
    """Verify that the read_dict function works correctly.
    Parameters: none
    Return: nothing
    """
    CUSTOMER_NUM_INDEX = 0

    # Verify that the read_dict function uses its filename
    # parameter by doing the following:
    # 1. Get a filename for a file that doesn't exist.
    # 2. Call the read_dict function with the filename.
    # 3. Verify that the open function inside the read_dict
    #    function raises a FileNotFoundError.
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        read_dict(filename, CUSTOMER_NUM_INDEX)
        pytest.fail("read_dict function must use its filename parameter")

    # Call the read_dict function and store the returned
    # dictionary in a variable named customers_dict.
    filename = path.join(path.dirname(__file__), "customers.csv")
    customers_dict = read_dict(filename, CUSTOMER_NUM_INDEX)

    # Verify that the read_dict function returns a dictionary.
    assert isinstance(customers_dict, dict), \
        "read_dict function must return a dictionary:" \
        f" expected a dictionary but found a {type(customers_dict)}"

    # Verify that the customers dictionry contains exactly 16 items.
    length = len(customers_dict)
    exp_len = 16
    assert length == exp_len, \
        "customers dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"

    # Check each item in the customers dictionary.
    check_customer(customers_dict, "D150", ["1 gallon milk", 2.85])
    check_customer(customers_dict, "D083", ["1 cup yogurt", 0.75])
    check_customer(customers_dict, "D215", ["1 lb cheddar cheese", 3.35])
    check_customer(customers_dict, "P019", ["iceberg lettuce", 1.15])
    check_customer(customers_dict, "P020", ["green leaf lettuce", 1.79])
    check_customer(customers_dict, "P021", ["butterhead lettuce", 1.83])
    check_customer(customers_dict, "P025", ["8 oz arugula", 2.19])
    check_customer(customers_dict, "P143", ["1 lb baby carrots", 1.39])
    check_customer(customers_dict, "W231", ["32 oz granola", 3.21])
    check_customer(customers_dict, "W112", ["wheat bread", 2.55])
    check_customer(customers_dict, "C013", ["twix candy bar", 0.85])
    check_customer(customers_dict, "H001", ["8 rolls toilet tissue", 6.45])
    check_customer(customers_dict, "H014", ["facial tissue", 2.49])
    check_customer(customers_dict, "H020", ["aluminum foil", 2.39])
    check_customer(customers_dict, "H021", ["12 oz dish soap", 3.19])
    check_customer(customers_dict, "H025", ["toilet cleaner", 4.50])


def check_customer(customers_dict, customer_number, expected_value):
    """Verify that the data for one customer number stored in the
    customers dictionary is correct.

    Parameters
        customers_dict: a dictionary that contains customer data
        customer_number: the customer number of the customer that this
            function will verify
        expected_value: the data that should be in the customers
            dictionary for the customer_number
    Return: nothing
    """
    assert customer_number in customers_dict
    actual_value = customers_dict[customer_number]
    length = len(actual_value)
    min_len = 2
    max_len = 3
    assert min_len <= length and length <= max_len, \
        f"value list for customer {customer_number} contains too" \
        f" {'few' if length < min_len else 'many'} elements:" \
        f" expected {min_len} or {max_len} elements but found {length}"

    if length == min_len:
        NAME_INDEX = 0
        PRICE_INDEX = 1
    else:
        NAME_INDEX = 1
        PRICE_INDEX = 2

    # Verify that the customer's name is correct.
    act_name = actual_value[NAME_INDEX]
    exp_name = expected_value[0]
    assert act_name == exp_name, \
        f"wrong name for customer {customer_number}: " \
        f"expected {exp_name} but found {act_name}"

    # Verify that the customer's price is correct.
    act_price = actual_value[PRICE_INDEX]
    if isinstance(act_price, str):
        act_price = float(act_price)
    exp_price = expected_value[1]
    assert act_price == approx(exp_price), \
        f"wrong price for customer {customer_number}: " \
        f"expected {exp_price} but found {act_price}"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
