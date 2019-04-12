# Jump Search
# Searches a sorted list in what is known as blocks, and then the correct block is searched using linear search. by correct block the block that holds the value you want to search for. An array/list is split into blocks, which is just a small section of the array/list, that is searched using linear search
# Sits in between binary and linear search as it uses linear when searching.
import math
class JumpSearchModel:

    def sort_list(self, list):
        list.sort()
        return list

    def search(self, list, list_size, search_for):
        jump = int(math.sqrt(list_size)) # block size to be jumped

        previous = 0

        print('jump = {}'.format(jump))
        while list[int(min(jump, list_size)-1)] < search_for: # while the index number of list is less than the value we're searching for or jump value is less than list_size loop will run
            previous = jump # previous is set to jump and used in linear search portion
            jump += int(math.sqrt(list_size)) # Jump is incremented to the next jump block
            if previous >= list_size: # if previous is greater than the size of the list then we've reached the end of the list without finding the value
                return -1
        # Linear Search
        while list[int(previous)] < search_for: # while number at list[previous] is less than the number we're searching for, keep searching
            previous += 1
            if previous == min(jump, list_size): # if we've reached the next block or the end of the list number not found
                return -1
        if list[int(previous)] == search_for: # if the list index previous matches the number we're searching for then return previous
            return previous
        return -1
