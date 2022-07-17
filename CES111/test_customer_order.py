
import pytest



def check_customer(customers_dict, customer_number):
    """Verify that the data for one customer number stored in the
    customers dictionary is correct.

    Parameters
        customers_dict: a dictionary that contains customer data
        customer_number: the customer number of the customer that this
            function will verify
    """
    assert customer_number in customers_dict
    actual_value = customers_dict[customer_number]
    length = len(actual_value)
    min_len = 1
    max_len = 2
    assert min_len <= length and length <= max_len, \
        f"value list for customer {customer_number} contains too" \
        f" {'few' if length < min_len else 'many'} elements:" \
        f" expected {min_len} or {max_len} elements but found {length}"

def test_always_passes():
    assert True

def test_always_fails():
    assert False
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
