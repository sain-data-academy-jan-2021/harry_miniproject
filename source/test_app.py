import unittest
from unittest.mock import patch, Mock

from app_databases import adding_for_loop
# from rebuild import index_choice, remove_list_operation, remove_from_list, update_list_operation, update_list, last_num, add_list_operation


# @patch('builtins.input')
# def test_index_choice(mock_input): # happy path
#     mock_input.return_value = '2'
#     expected = 1
#     actual = index_choice('remove')
#     assert expected == actual
    
# def test_remove_list_operation(): # happy path
#     list = ['1', '2', '3']
#     index = 1
#     expected = ['1', '3']
#     actual = remove_list_operation(list, index)
#     assert expected == actual

# @patch('builtins.input')    
# def test_remove_from_list(mock_input): # happy path
#     list = ['1', '2', '3']
#     mock_input.return_value = '2'
#     expected = ['1', '3']
#     actual = remove_from_list(list)
#     assert expected == actual
        
# def test_update_list_operation(): # happy path
#     list = [{'a': '1', 'b': "2", 'c': '3'}]
#     index = 0
#     key = 'a'
#     new_value = 'new_value' 
#     expected = [{'a': 'new_value', 'b': "2", 'c': '3'}]
#     actual = update_list_operation(list, index, key, new_value)
#     assert expected == actual

# @patch('builtins.input')    
# def test_update_list(mock_input): # happy path
#     list = [{'Index': '1', 'Name': 'Cake', 'Price': '0.4'}]
#     mock_input.side_effect = ['1', '', '0.99']
#     expected = [{'Index': '1', 'Name': 'Cake', 'Price': '0.99'}]
#     actual = update_list(list)
#     assert expected == actual

# def test_last_num_with_an_empty_list(): # happy path
#     list = []
#     expected = '1'
#     actual = last_num(list)
#     assert expected == actual

# def test_last_num_with_an_existing_list(): # happy path
#     list = [{'Index': '1', 'Name': 'Cake', 'Price': '0.4'}]
#     expected = '2'
#     actual = last_num(list)
#     assert expected == actual
    
# @patch('builtins.input')    
# def test_add_list_operation(mock_input): # happy test
#     list = [{'Index': '1', 'Name': 'Cake', 'Price': '0.4'}]
#     mock_input.side_effect = ['Soda', '0.75']
#     expected = {'Index': '2', 'Name': 'Soda', 'Price': '0.75'}
#     actual = add_list_operation(list)
#     assert expected == actual
    
class TestDatabaseMethods(unittest.TestCase):
    
    # def test_function(self):
    #     expected = something
    #     actual = function to test
    #     self.assertEqual(expected, actual)
    

    @patch("builtins.input")
    @patch("app_databases.execute_database_query")
    def test_adding_for_loop(self, mock_execute, mock_input):

    # Assemble
        table = 'products'
        columns = ['product_name', 'product_price']
        mock_input.side_effect = ['Soda', '0.75']   
        expected = 'INSERT INTO products (product_name, product_price) VALUES ("Soda", "0.75")'
    
    # Act
        adding_for_loop(columns, table)

    # Assert
        mock_execute.assert_called_with(expected)

    @patch("builtins.input")
    @patch("app_databases.execute_database_query")
    def test_adding_for_loop_and_drop_out(self, mock_execute, mock_input):

    # Assemble
        table = 'products'
        columns = ['product_name', 'product_price']
        mock_input.side_effect = ['0']
    
    # Act
        adding_for_loop(columns, table)

    # Assert
        assert mock_execute.call_count == 0


    @patch("builtins.input")
    @patch("app_databases.execute_database_query")
    def test_adding_orders_for_loop(self, mock_execute, mock_input):

    # Assemble
        table = 'orders'
        columns = ['customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
        mock_input.side_effect = ['ABC', '123', '12Highst','12']   
        expected = 'INSERT INTO orders (customer_name, customer_number, customer_address, status, courier_id) VALUES ("Abc", "123", "12Highst", "Preparing", "12")'
    
    # Act
        adding_for_loop(columns, table)

    # Assert
        mock_execute.assert_called_with(expected)


if __name__ == '__main__': 
    unittest.main()