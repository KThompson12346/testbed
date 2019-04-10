class BinarySearchModel:

    def sort_arr(self, list): # Uses library function to sort list
        list.sort()
        return list

    def search(self, list, list_start, list_end, search_for):
        if list_end >= list_start:

            mid_point = int(list_start + (list_end - list_start) / 2)

            if list[mid_point] == search_for:
                return mid_point

            elif list[mid_point] > search_for:
                return self.search(list, list_start, mid_point-1, search_for)

            else:
                return self.search(list, mid_point+1, list_end, search_for)

        else:
            return -1
