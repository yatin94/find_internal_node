try:
    import unittest
    from internal_node import find_internal_nodes_num
except Exception as exec:
    print(f"Import module error {str(exec)}")



class InternalNodeTestCase(unittest.TestCase):
    
    def test_internal_node_1(self):
        input_tree = [4, 4, 1, 5, -1, 4, 5]
        return_node_sum = find_internal_nodes_num(input_tree)
        self.assertEqual(return_node_sum, 3)

    def test_internal_node_2(self):
        input_tree = [3,4,3,-1,3]
        return_node_sum = find_internal_nodes_num(input_tree)
        self.assertEqual(return_node_sum, 2)

    def test_internal_node_3(self):
        input_tree = [-1, 0, 1, 2, 3]
        return_node_sum = find_internal_nodes_num(input_tree)
        self.assertEqual(return_node_sum, 4)

    def test_internal_node_3(self):
        input_tree = [-1]
        return_node_sum = find_internal_nodes_num(input_tree)
        self.assertEqual(return_node_sum, 0)

    def test_internal_node_4(self):
        input_tree = [3,3,3,-1,3,0,1,5,4,6]
        return_node_sum = find_internal_nodes_num(input_tree)
        self.assertEqual(return_node_sum, 6)

    def test_internal_node_5(self):
        input_tree = []
        return_node_sum = find_internal_nodes_num(input_tree)
        self.assertEqual(return_node_sum, 0)



if __name__ == "__main__":
    unittest.main()