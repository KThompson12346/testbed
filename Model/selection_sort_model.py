# Selection Sort
# Continuously selects the lowest value in the array/list and moves it into the
# first position of the array/list, as this is done a sorted array is built up
# from the first position as elements  are moved into the first element and
# shifted up in the array/list.

class SelectionSortModel:

    def selection_sort(self, list):
        for i in range(len(list)): # will loop through all the elements in the list
            min_index = i
            for j in range(i+1, len(list)): # will loop through the 'unsorted' portion of the list
                if list[min_index] > list[j]: # if minimum index is bigger than first item in unsorted list min_index is set to j to be new minimum index
                    min_index = j # j is the index after min_index
            # the minimum (smallest) element is swapped with the first element of the sorted list
            temp = list[i]
            list[i] = list[min_index]
            list[min_index] = temp
