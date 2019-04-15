# Merge Sort
# A divide and conquer algorithm that will split an array in half recursively
# until each element is in an array/list of its own (i.e. an array/list of length
# one). Once split into single element arrays/lists each element is merged
# back together in stages and while being merged the elements are sorted in order.
# When merging, the smallest value is merged first.

class MergeSortModel:

    def merge_sort(self, list):
        if len(list) > 1:
            mid_point = len(list) // 2 # finding the mid point of the list
            left_side = list[:mid_point] # first half of list
            right_side = list[mid_point:] # second half of list

            self.merge_sort(left_side)
            self.merge_sort(right_side)

            left = 0 # index for the left side of list
            right = 0 # index for the right side of list
            new = 0 # index for the newly sorted list

            while left < len(left_side) and right < len(right_side): # will keep looping until the end of both the left_side and right_side of list has been met
                if left_side[left] < right_side[right]: # compares elements from left side with right side of the list and places smallest element into list
                    list[new] = left_side[left] # puts left_side element into the new sorted list
                    left += 1
                else:
                    list[new] = right_side[right] # puts right_side element into the new sorted list
                    right += 1
                new += 1 # on either of the cases 'new' index is incremented

            # last two while loops check that both sides of the list have been complete emptied and no elements are left standing, a clean up check
            while left < len(left_side):
                list[new] = left_side[left]
                left += 1
                new += 1

            while right < len(right_side):
                list[new] = right_side[right]
                right += 1
                new += 1
        return list
