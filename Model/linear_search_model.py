class LinearSearchModel:

    def search(self, arr, up_to, search_for):
        for i in range(0, up_to):
            if arr[i] == search_for:
                return i
        return -1
