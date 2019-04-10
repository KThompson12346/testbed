class LinearSearchModel:

    def search(self, list, list_len, search_for):
        for i in range(0, list_len):
            if list[i] == search_for:
                return i
        return -1
