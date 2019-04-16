# Quick sort
# A divide and conquer algorithm that recursively calls itself on the sets of
# the list. it uses a pivot value that can be choosen in different ways. the pivot
# value is used by the partition function that moves values smaller than the pivot
# to the left of the pivot, and values bigger to the right of the pivot. This Quick
# sort takes a pivot value of the highest element in the list.

class QuickSortModel:

    def partition(self, list, start, end):
        i = (start - 1) # index of smaller element
        print('i = {}'.format(i))
        pivot = list[end] # last element is choosen as the pivot

        for j in range(start, end): # will loop through the whole array
            if list[j] <= pivot: # checks if items are less than the pivot if so puts them to the left of the pivot
                i += 1 # increments i after each iteration
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
        # bigger elements are put to the right of the pivot
        temp = list[i+1]
        list[i+1] = list[end]
        list[end] = temp
        print('i+1 is {}'.format(i+1))
        return i+1 # returns the pivot in its correct order

    def quick_sort(self, list, start, end):
        if start < end:
            pivot = self.partition(list, start, end)
            self.quick_sort(list, start, pivot-1)
            self.quick_sort(list, pivot+1, end)
