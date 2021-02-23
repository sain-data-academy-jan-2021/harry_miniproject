import unittest
from unittest.mock import patch, Mock
from app_databases import choose_order_items, add_to_basket, remove_database_function, update_order_status, columns_and_values

class TestDatabaseMethods(unittest.TestCase):

    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_choose_order_items(self, mock_input, mock_execute):
        mock_execute.return_value = ((1,), (2,))
        mock_input.side_effect = ['1', '0']
        expected = ['1']
        
        actual = choose_order_items()
        
        assert expected == actual


    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_choose_multiple_order_items(self, mock_input, mock_execute):
        mock_execute.return_value = ((1,), (2,))
        mock_input.side_effect = ['1', '2', '0']
        expected = ['1', '2']
        
        actual = choose_order_items()
        
        assert expected == actual
    
    
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_choose_an_number_that_does_not_exist(self, mock_input, mock_execute):
        mock_execute.return_value = ((1,), (2,))
        mock_input.side_effect = ['1', '3', '0']
        expected = ['1']
        
        actual = choose_order_items()
        
        assert expected == actual
    
    
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_choose_a_letter_that_does_not_exist(self, mock_input, mock_execute):
        mock_execute.return_value = ((1,), (2,))
        mock_input.side_effect = ['1', 'w', '0']
        expected = ['1']
        
        actual = choose_order_items()
        
        assert expected == actual
        
#-----------------------------------------------------

    @patch('app_databases.execute_sql_select')
    @patch('app_databases.choose_order_items')
    @patch('app_databases.execute_sql_update')
    def test_add_to_basket(self, mock_execute_update, mock_choose, mock_execute_select):
        mock_execute_select.return_value = ((7,),)
        mock_choose.return_value = ['1']
        expected = 'INSERT INTO customer_orders (order_id, product_id) VALUES (7, 1)'

        add_to_basket()
        
        mock_execute_update.assert_called_with(expected)
        
#-----------------------------------------------------

    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('app_databases.execute_sql_update')
    def test_remove_from_product_database_function(self, mock_execute, mock_existing_id, mock_get_column):      
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']
        mock_existing_id.return_value = '1'
        expected = 'DELETE FROM products WHERE product_id = 1'
        
        remove_database_function(table)
        
        mock_execute.assert_called_with(expected)
    
    
    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('app_databases.execute_sql_update')
    def test_remove_from_couriers_database_function(self, mock_execute, mock_existing_id, mock_get_column):      
        table = 'couriers'
        mock_get_column.return_value = ['courier_id', 'courier_name']
        mock_existing_id.return_value = '1'
        expected = 'DELETE FROM couriers WHERE courier_id = 1'
        
        remove_database_function(table)
        
        mock_execute.assert_called_with(expected)
        
    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('app_databases.execute_sql_update')
    def test_remove_an_order_from_a_database(self, mock_execute, mock_existing_id, mock_get_column):      
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name']
        mock_existing_id.return_value = '1'
        expected = 'DELETE FROM customer_orders WHERE order_id = 1'
        
        remove_database_function(table)
        
        mock_execute.assert_called_with(expected)   
        mock_execute.call_count == 2
        
#---------------------------------------------------------     
    @patch('app_databases.choose_an_existing_id') 
    @patch('builtins.input')   
    @patch('app_databases.execute_sql_update')
    def test_update_order_status(self, mock_execute, mock_input, mock_existing_id):
        mock_existing_id.return_value = '1'
        mock_input.return_value = 'Cancelled'
        expected = 'UPDATE orders SET status = "Cancelled" WHERE order_id = 1'
        
        update_order_status()
        
        mock_execute.assert_called_with(expected)
        
    @patch('app_databases.choose_an_existing_id') 
    @patch('builtins.input')   
    @patch('app_databases.execute_sql_update')
    def test_update_order_status_with_wrong_status(self, mock_execute, mock_input, mock_existing_id):
        mock_existing_id.return_value = '1'
        mock_input.side_effect = ['Pending', 'Cancelled']
        expected = 'UPDATE orders SET status = "Cancelled" WHERE order_id = 1'
        
        update_order_status()
        
        mock_execute.assert_called_with(expected)    
        

    @patch('app_databases.choose_an_existing_id') 
    @patch('builtins.input')   
    @patch('app_databases.execute_sql_update')
    def test_update_order_status_with_number(self, mock_execute, mock_input, mock_existing_id):
        mock_existing_id.return_value = '1'
        mock_input.side_effect = ['1', 'Cancelled']
        expected = 'UPDATE orders SET status = "Cancelled" WHERE order_id = 1'
        
        update_order_status()
        
        mock_execute.assert_called_with(expected) 

#--------------------------------------------------

    def test_columns_and_values(self):
        column_names = ['product_name', 'product_price']
        string_of_values = ''
        string_of_columns = ''
        column = 'product_name'
        value = 'Orange'
        expected = "product_name, ", '"Orange", '
        
        actual = columns_and_values(column, value, column_names, string_of_values, string_of_columns)
        
        self.assertEqual (actual, expected)
    
    
    def test_final_columns_and_values(self):
        column_names = ['product_name', 'product_price']
        string_of_values = ''
        string_of_columns = ''
        column = 'product_price'
        value = '4.3'
        expected = "product_price", '"4.3"'
        
        actual = columns_and_values(column, value, column_names, string_of_values, string_of_columns)
        
        self.assertEqual (actual, expected)
    
    
    
    
    
    
    
    
    
    
    
    
    
              
    # @patch('builtins.input')
    # @patch('app_databases.execute_database_query')
    # def test_adding_for_loop(self, mock_execute, mock_input):

    # # Assemble
    #     table = 'products'
    #     columns = ['product_name', 'product_price']
    #     mock_input.side_effect = ['Soda', '0.75']   
    #     expected = 'INSERT INTO products (product_name, product_price) VALUES ('Soda', '0.75')'
    
    # # Act
    #     adding_for_loop(columns, table)

    # # Assert
    #     mock_execute.assert_called_with(expected)

    # @patch('builtins.input')
    # @patch('app_databases.execute_database_query')
    # def test_adding_for_loop_and_drop_out(self, mock_execute, mock_input):

    # # Assemble
    #     table = 'products'
    #     columns = ['product_name', 'product_price']
    #     mock_input.side_effect = ['0']
    
    # # Act
    #     adding_for_loop(columns, table)

    # # Assert
    #     assert mock_execute.call_count == 0


    # @patch('builtins.input')
    # @patch('app_databases.execute_database_query')
    # def test_adding_orders_for_loop(self, mock_execute, mock_input):

    # # Assemble
    #     table = 'orders'
    #     columns = ['customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
    #     mock_input.side_effect = ['ABC', '123', '12Highst','12']   
    #     expected = 'INSERT INTO orders (customer_name, customer_number, customer_address, status, courier_id) VALUES ('Abc', '123', '12Highst', 'Preparing', '12')'
    
    # # Act
    #     adding_for_loop(columns, table)

    # # Assert
    #     mock_execute.assert_called_with(expected)


if __name__ == '__main__': 
    unittest.main()