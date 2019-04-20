import random
class Controller:


    def initialize_list_elements(self, num_of_elements, up_to):
        numbers_list = [] # is the list of elements that will be used by the searching and sorting algorithms
        for _ in range(num_of_elements):
            numbers_list.append(random.randint(1, up_to))
        return numbers_list

    def reset_list(self, list):
        list.clear()
        return list

    def print_list(self, list):
        print('list elements = {}'.format(list))
