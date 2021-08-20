import os as os
import pickle as pickle


class Element:
    def __init__(self, name='', count=1):
        self.name = name
        self.count = count

el1 = Element(name='first', count=1)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(el1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PickleClassTest')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
