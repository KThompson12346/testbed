import random
import sys, os.path
view_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/View/')
sys.path.append(view_dir)
import view


class Controller:

    def initialize_list_elements(self, num_of_elements, up_to):
        numbers_list = [] # is the list of elements that will be used by the searching and sorting algorithms
        for _ in range(num_of_elements):
            numbers_list.append(random.randint(1, up_to))
        return numbers_list

    def random_colour_code(self):
        hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        colour_code = '#'
        for i in range(0,6):
            colour_code = colour_code + choice(hex_chars)
        return colour_code

    def animation(self, my_list):
        x = 220
        y = 500
        bar_width = 15
        for item in my_list:
            bar = view.canvas.create_rectangle(x, y, x+barwidth, y-(item*15), fill=random_colour_code())
            x += bar_width + 5
            time.sleep(0.2)
            view.canvas.update()

    def clear_list(self, list):
        list.clear()
        return list

    def print_list(self, list):
        print('list elements = {}'.format(list))

view = view.View()
view.window.mainloop()
