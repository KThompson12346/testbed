# Heap Sort
# Is a comparison based sorting algorithm that uses the binary heap data structure. Binary heap is a
# binary tree that is complete binary tree (a binary tree where every level is filled and leaf
# elements lean towards the left and bottom leaf elements may not have a right sibling) but the
# items are stored in a special order where the parent node is either always greater than (max heap)
# or smaller than (min heap) its children.

class HeapSortModel:

    def make_heap(self, list, heap_size, root): # root is the initial root will change accordingly
        root_value = root # root of heap
        left = 2 * root + 1 # left child
        right = 2 * root + 2 # right child

        if left < heap_size and list[root] < list[left]: # checks if root has a left child and if root is smaller than its left child
            root_value = left # assigns the root as the left child

        if right < heap_size and list[root_value] < list[right]: # checks if root has a right child and if root is smaller than its right child
            root_value = right # assigns the root as the right child
        # if the root_value is not the largest element in the list (i.e. the root) then the root_value is assigned a value, which is the root
        if root_value != root:
            temp = list[root]
            list[root] = list[root_value]
            list[root_value] = temp
        # then make_heap is called again with the root_value as the root element and whole list becomes a max heap binary tree
             self.make_heap(list, heap_size, root_value)

    def heap_sort(self, list):
        size_of_list = len(list)
        # first loop creates a heap from the bottom up
        for i in range(size_of_list, -1, -1):
            self.make_heap(list, size_of_list, i)
        # takes elements out one by one starting from last element the smallest
        for j in range(size_of_list-1, 0, -1):
            temp = list[j]
            list[j] = list[0]
            list[0] = temp
            self.make_heap(list, j, 0)
        return list
