import os as os
import pickle as pickle
from dataclasses import dataclass, field
from random import randint

file_name = '.options.pickle'
range_min = 3
range_max = 12


@dataclass
class Element:
    name: str
    count: int

    def __post_init__(self):
        pass

    def show(self):
        return f"{self.name} count: {self.count}"


@dataclass
class RescuerData:
    ver_no: str = field(init=False)

    email_my: str
    email_your: str

    elements: dict[int: Element] = field(init=False, compare=False)

    def __init__(self):
        ver_no = '20210821'

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

    def elements_fill(self):
        dic: dict[int: Element]

        dic = {1: Element(name='first', count=1)}
        dic |= {2: Element(name='second', count=10)}
        dic |= {3: Element(name='third', count=3)}

        RescuerData.elements = dic
        RescuerData.elements.update({4: Element(name='thirds', count=30)})
        RescuerData.email_my = 'my e-mail'
        main_data.email_your = 'your e-mail'


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
        print_dic(main_data.elements)

        main_data.write_data()

    print('Count of records written : ', len(main_data.elements))
# не работает совсем
#    print('Count of records written : ', main_data.elements_count())
    print('E-mail my: ', main_data.email_my)
    print('E-mail your: ', main_data.email_your)

