# Insertion sort
# Sorts array/list elements into a sorted portion of an array/list by taking an
# element and comparing with the sorted portion of the array/list and inserting
# the element into the correct position of the sorted portion which starts with
# position 0 being the regarded as the sorted portion and grows as elements are
# compared and inserted
class InsertionSortModel:

    def insertion_sort(self, list):
        for unsorted in range(1, len(list)): # starts at the second item in the list onward i.e. the unsorted portion
            for sorted in range(unsorted-1, 0, -1): # starts at the item directly before unsorted and moves backwards to 0 index i.e. the sorted portion where elemenets are inserted
                if list[sorted] > list[sorted+1]: # list[sorted+1] corresponds to the first unsorted element of the array but is counted as sorted and inserted into the correct position of sorted list
                    # list[sorted] is swapped until its in the right place
                    temp = list[sorted+1]
                    list[sorted+1] = list[sorted]
                    list[sorted] = temp
                else:
                    break
        return list
