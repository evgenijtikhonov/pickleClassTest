import os as os
import pickle as pickle
from dataclasses import dataclass, field

file_name = 'options.pickle'


class Element:

    def __init__(self, name='', count=1):
        self.name = name
        self.count = count

    def show(self):
        return f"{self.name} count: {self.count}"


class RescuerData:
    ver_no = '20210821'

    email_my = ''
    email_your = ''

    elements: dict[int: Element] = {}

    def __init__(self):
        pass

    def write_data(self):
        try:
            with open(file_name, 'wb') as f:
                pickle.dump(self, f)
        except Exception as Id:
            print(f'Ошибка записи файла options ({Id})')
        else:
            print('Written!')

    def elements_count(self):
        print(elements[1])
#        return len(RescuerData.elements)

    @staticmethod
    def read_data():
        if os.path.isfile(file_name):
            try:
                with open(file_name, 'rb') as f:
                    md = pickle.load(f)
            except Exception as Id:
                print(f'Ошибка чтения файла options ({Id})')
                return None
            else:
                return md


def elements_fill():
    dic: dict[int: Element]

    dic = {1: Element(name='first', count=1)}
    dic |= {2: Element(name='second', count=10)}
    dic |= {3: Element(name='third', count=3)}

    RescuerData.elements = dic
    RescuerData.elements.update({4: Element(name='thirds', count=30)})
    RescuerData.email_my = 'my e-mail'
    main_data.email_you = 'your e-mail'


def print_dic(d):
    for key, value in d.items():
        print(f"{key} -> ", value.show())


if __name__ == '__main__':
    main_data = None

    if os.path.isfile(file_name):
        try:
            main_data = RescuerData.read_data()
            print_dic(RescuerData.elements)
            print('Read data!')
#            print('Count of records read : ', RescuerData.elements_count())
            print('Version of data: ', RescuerData.ver_no)
            print('E-mail my: ', RescuerData.email_my)
        except Exception as Id:
            print(f'Ошибка чтения файла options ({Id})')
            main_data = None

    if main_data is None:
        main_data = RescuerData()
        elements_fill()
        print_dic(RescuerData.elements)

        main_data.write_data()

    print('Count of records written : ', len(RescuerData.elements))
# не работает совсем
#    print('Count of records written : ', main_data.elements_count())
    print('E-mail my: ', RescuerData.email_my)

