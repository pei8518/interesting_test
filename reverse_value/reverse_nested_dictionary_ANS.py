# -*- coding: utf-8 -*-
import unittest

def rever_value():
    # Input:
    input_value = {
        'hired': {
            'be': {
                'to': {
                    'deserve': 'I'
                }
            }
        }      
    }

    def recursive_items(dictionary):
        for key, value in dictionary.items():
            # print(key, value)
            if type(value) is dict:
                str_lst.append(key)
                yield from recursive_items(value)
            else:
                str_lst.append(key)
                str_lst.append(value)
                yield (key, value)

    #reverse the dictionary
    def reverse_dict(input_lst):
        tree_dict = {}
        # str_num = len(input_lst)
        tree_dict = {input_lst[1]: input_lst[0]}
        for i in range(2, len(input_lst)):
            key = input_lst[i]
            # print(key)
            tree_dict = {key: tree_dict}
            # print(tree_dict)

        return tree_dict

    str_lst = []
    for key, value in recursive_items(input_value):
        print(key, value)
    
    output_dict = reverse_dict(str_lst)

    return output_dict

#test 
# output_value = {
#   'I': {
#     'deserve': {
#       'to': {
#          'be': 'hired'
#       }
#     }
#   }
# }
# aaa = rever_value()
# output_dict == output_value

class reverseTest(unittest.TestCase):

    def test_reverse_value(self):       
        output = rever_value()
        output_value = {
            'I': {
                'deserve': {
                    'to': {
                        'be': 'hired'
                    }
                }
            }
        }        

        self.assertEqual(output, output_value) 

# if __name__ == '__main__':
#  unittest.main()