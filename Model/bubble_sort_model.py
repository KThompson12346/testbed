# Bubble sort
# bubble sort is a simple sorting algorithm that simply swaps the elements until they are all sorted in order
# it makes numerous passes through an array/list comparing one element at a time eventually placing it in the
# correct place
import sys, os.path
controller_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/Controller/')
sys.path.append(controller_dir)
import controller

class BubbleSortModel:

    def bubble_sort(self, list):
        for passes in range(len(list)): # counts the number of passes that bubble sort is on (0-7)
            for i in range(0, len(list)-passes-1): # loop for the comparison of the elements excludes the sorted (end) portion of the array/list
                if list[i] > list[i+1]: # if element at i is bigger than the next element (i+1) the items are swapped
                    temp = list[i+1]
                    list[i+1] = list[i]
                    list[i] = temp
        return list
