import unittest
from unittest.mock import patch, Mock, call
from app_databases import choose_order_items, add_to_basket, remove_database_function, update_order_status, columns_and_values, existing_products, add_to_database_function, choose_an_existing_id, update_database_function, update_basket

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
        self.assertEqual(mock_execute.call_count, 2)
    
    
    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('app_databases.execute_sql_update')
    def test_cancel_remove_an_order_from_a_database_function(self, mock_execute, mock_existing_id, mock_get_column):      
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name']
        mock_existing_id.return_value = '0'
        
        remove_database_function(table)
          
        self.assertEqual(mock_execute.call_count, 0)
        
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
    
#----------------------------------------------------
    
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_new_product_in_existing_products_functions(self, mock_input, mock_execute):
        mock_execute.return_value = (('Fanta',), ('Cake',), ('Cookies',), ('Apple',))
        mock_input.return_value = 'Kiwi'
        expected = 'Kiwi'
        
        actual = existing_products()
        
        self.assertEqual (actual, expected)
    
    
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_existing_product_in_existing_products_functions(self, mock_input, mock_execute):
        mock_execute.return_value = (('Fanta',), ('Cake',), ('Cookies',), ('Apple',))
        mock_input.side_effect = ['Fanta', 'Kiwi']
        expected = 'Kiwi'
        
        actual = existing_products()
        
        self.assertEqual (actual, expected)
    
    
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_cancel_in_existing_products_functions(self, mock_input, mock_execute):
        mock_execute.return_value = (('Fanta',), ('Cake',), ('Cookies',), ('Apple',))
        mock_input.return_value = '0'
        expected = '0'
        
        actual = existing_products()
        
        self.assertEqual (actual, expected)
    
    
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_existing_product_then_cancel_in_existing_products_functions(self, mock_input, mock_execute):
        mock_execute.return_value = (('Fanta',), ('Cake',), ('Cookies',), ('Apple',))
        mock_input.side_effect = ['Fanta', '0']
        expected = '0'
        
        actual = existing_products()
        
        self.assertEqual (actual, expected)
    
#-----------------------------------------------------------
    
    @patch('app_databases.get_column_names')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    @patch('app_databases.add_to_basket')  
    def test_add_courier_to_database_function(self, mock_basket, mock_execute, mock_input, mock_get_column):
        table = 'couriers'
        mock_get_column.return_value = ['courier_id', 'courier_name', 'phone_number']     
        mock_input.side_effect = ['Ben', '07123456789']
        expected = 'INSERT INTO couriers (courier_name, phone_number) VALUES ("Ben", "07123456789")'
        
        add_to_database_function(table)
              
        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_basket.call_count, 0)
              
    @patch('app_databases.get_column_names')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_cancel_while_adding_courier_to_database_function(self, mock_execute, mock_input, mock_get_column):
        table = 'couriers'
        mock_get_column.return_value = ['courier_id', 'courier_name', 'phone_number']     
        mock_input.side_effect = ['Ben', '0']
        
        add_to_database_function(table)
              
        self.assertEqual(mock_execute.call_count, 0)    
              
              
    @patch('app_databases.get_column_names')
    @patch('app_databases.existing_products')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')  
    @patch('app_databases.add_to_basket')         
    def test_add_product_to_database_function(self, mock_basket, mock_execute, mock_input, mock_existing_product, mock_get_column):           
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']     
        mock_existing_product.return_value = 'Orange'
        mock_input.return_value = '4.3'
        expected = 'INSERT INTO products (product_name, product_price) VALUES ("Orange", "4.3")'
        
        add_to_database_function(table)
              
        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_basket.call_count, 0)
              
              
    @patch('app_databases.get_column_names')
    @patch('app_databases.existing_products')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')          
    def test_cancel_while_adding_product_to_database_function(self, mock_execute, mock_input, mock_existing_product, mock_get_column):           
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']     
        mock_existing_product.return_value = '0'
        
        add_to_database_function(table)
              
        self.assertEqual(mock_execute.call_count, 0)
              
              
    @patch('app_databases.get_column_names')
    @patch('builtins.input')
    @patch('app_databases.choose_an_existing_id')
    @patch('app_databases.execute_sql_update')  
    @patch('app_databases.add_to_basket')        
    def test_add_order_to_database_function(self, mock_basket, mock_execute, mock_existing_courier, mock_input,  mock_get_column):           
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']     
        mock_existing_courier.return_value = '12'
        mock_input.side_effect = ['ABC', '123', '12Highst']   
        expected = 'INSERT INTO orders (customer_name, customer_number, customer_address, status, courier_id) VALUES ("Abc", "123", "12Highst", "Preparing", "12")'
        mock_basket.return_value = ['1']
        add_to_database_function(table)
              
        mock_execute.assert_called_with(expected)   
        self.assertEqual(mock_basket.call_count, 1)  
              
              
    @patch('app_databases.get_column_names')
    @patch('builtins.input')
    @patch('app_databases.choose_an_existing_id')
    @patch('app_databases.execute_sql_update')  
    @patch('app_databases.add_to_basket')        
    def test_cancel_while_adding_order_to_database_function(self, mock_basket, mock_execute, mock_existing_courier, mock_input,  mock_get_column):           
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']     
        mock_existing_courier.return_value = '0'
        mock_input.side_effect = ['ABC', '123', '12Highst']   
        
        add_to_database_function(table)
               
        self.assertEqual(mock_execute.call_count, 0)
  
#------------------------------------------------------------
    @patch('app_databases.get_column_names')
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_choose_an_existing_id(self,mock_input, mock_existing_id, mock_get_column):
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']
        mock_existing_id.return_value = ((1,), (2,))
        mock_input.return_value = '1'
        expected = 1
        
        actual = choose_an_existing_id(table)
        
        self.assertEqual (actual, expected)
              
              
    @patch('app_databases.get_column_names')
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_a_non_id_select_with_choose_an_existing_id(self,mock_input, mock_existing_id, mock_get_column):
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']
        mock_existing_id.return_value = ((1,), (2,))
        mock_input.side_effect = ['3', '1']
        expected = 1
        
        actual = choose_an_existing_id(table)
        
        self.assertEqual (actual, expected)        
              
              
    @patch('app_databases.get_column_names')
    @patch('app_databases.execute_sql_select')
    @patch('builtins.input')
    def test_cancelling_out_of_choose_an_existing_id(self,mock_input, mock_existing_id, mock_get_column):
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']
        mock_existing_id.return_value = ((1,), (2,))
        mock_input.return_value = '0'
        expected = '0'
        
        actual = choose_an_existing_id(table)
        
        self.assertEqual (actual, expected)        

#-------------------------------------------------------------

    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_products(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'products'
        mock_get_column.return_value = ['product_id', 'product_name', 'product_price']
        mock_id.return_value = '1'
        mock_input.side_effect = ['', '2.50']
        expected = 'UPDATE products SET product_price = "2.50" WHERE product_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 1)


    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_cancelling_out_of_update_database_function(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'couriers'
        mock_get_column.return_value = ['courier_id', 'courier_name', 'phone_number']
        mock_id.return_value = '0'

        update_database_function(table)

        self.assertEqual(mock_execute.call_count, 0)


    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_couriers(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'couriers'
        mock_get_column.return_value = ['courier_id', 'courier_name', 'phone_number']
        mock_id.return_value = '1'
        mock_input.side_effect = ['', '07123456789']
        expected = 'UPDATE couriers SET phone_number = "07123456789" WHERE courier_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 1)


    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_orders(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
        mock_id.return_value = '1'
        mock_input.side_effect = ['Richard', '', '', '2']
        expected = 'UPDATE orders SET courier_id = "2" WHERE order_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 2)


    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_orders_without_passes(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
        mock_id.return_value = '1'
        mock_input.side_effect = ['Richard', '07123456789', '123 Main St', '2']
        expected = 'UPDATE orders SET courier_id = "2" WHERE order_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 4)


    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_orders_third_loop_expected(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
        mock_id.return_value = '1'
        mock_input.side_effect = ['Richard', '07123456789', '123 Main St', '']
        expected = 'UPDATE orders SET customer_address = "123 Main St" WHERE order_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 3)
    
    
    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_orders_second_loop_expected(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
        mock_id.return_value = '1'
        mock_input.side_effect = ['Richard', '07123456789', '', '']
        expected = 'UPDATE orders SET customer_number = "07123456789" WHERE order_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 2)


    @patch('app_databases.get_column_names')
    @patch('app_databases.choose_an_existing_id')
    @patch('builtins.input')
    @patch('app_databases.execute_sql_update')
    def test_update_database_function_with_orders_first_loop_expected(self, mock_execute, mock_input, mock_id, mock_get_column):
        table = 'orders'
        mock_get_column.return_value = ['order_id', 'customer_name', 'customer_number', 'customer_address', 'status', 'courier_id']
        mock_id.return_value = '1'
        mock_input.side_effect = ['Richard', '', '', '']
        expected = 'UPDATE orders SET customer_name = "Richard" WHERE order_id = 1'

        update_database_function(table)

        mock_execute.assert_called_with(expected)
        self.assertEqual(mock_execute.call_count, 1)

#------------------------------------------------------

    # @patch('app_databases.choose_an_existing_id')
    # @patch('app_databases.read_from_database')
    # @patch('app_databases.execute_sql_update')
    # @patch('app_databases.choose_order_items')
    # def test_update_basket(self, mock_basket, mock_execute, mock_read, mock_id):
    #     mock_id.return_value = 1
    #     mock_read.return_value = [{'product_id': 1, 'product_name': 'Fanta', 'product_price': '2.99'}, {'product_id': 5, 'product_name': 'Apple', 'product_price': '0.30'}]
    #     mock_basket = ['1', '2']
    #     expected2 = 'INSERT INTO customer_orders (order_id, product_id) VALUES (1, "2")'
    #     expected1 = 'DELETE FROM customer_orders WHERE order_id = 1'
        
    #     update_basket()
    #     # mock_execute.assert_has_calls([call(self.expected), call(self.val)])
    #     mock_execute.assert_has_calls([call(expected1), call(expected2)])

    #     # mock_execute.assert_called_with(expected)
    #     # self.assertEqual(mock_execute.call_count, 3)


if __name__ == '__main__': 
    unittest.main()