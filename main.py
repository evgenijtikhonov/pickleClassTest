import os as os
import pickle as pickle
from dataclasses import dataclass, field
from random import randint, choice
from names import names, mails

file_name = '.options.pickle'
range_min = 3
range_max = 12

names_size = len(names)


@dataclass
class Element:
    name: str
    count: int
    email: str

    def __post_init__(self):
        pass

    def show(self):# уже не используется
        return f"{self.name} count: {self.count}"


@dataclass
class RescuerData:
    ver_no: str = field(init=False)
    read_count: int = field(init=False)

    email_my: str
    email_your: str

    elements: dict[int: Element] = field(init=False, compare=False)

    def __post_init__(self):
        self.ver_no = '20210821'
        self.elements = {}
        self.read_count = 0

    def write_data(self):
        try:
            with open(file_name, 'wb') as f:
                pickle.dump(self, f)
        except Exception as Id:
            print(f'Ошибка записи файла options ({Id})')
        else:
            print('Written!')

    def elements_count(self):
        return len(self.elements)

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
                if md.read_count > randint(0, 3):
                    print('Excuse me, this is a chance...')
                    return None
                else:
                    md.read_count += 1
                    md.write_data()
                    return md

    def elements_fill(self):
        times = randint(range_min, range_max)

        for one in range(times):
            name = choice(names)
            self.elements.update({one + 1: Element(name=name,
                                                   count=randint(1, names_size),
                                                   email=name.lower()+'@'+choice(mails))})
        self.email_my = 'my e-mail'
        self.email_your = 'your e-mail'


    def print_dic(self):
        for key, value in self.elements.items():
            #print(f"{key} -> ", value.show())
            print(value)


if __name__ == '__main__':
    main_data = None

    if os.path.isfile(file_name):
        try:
            main_data = RescuerData.read_data()

            main_data.print_dic()
            print('Read data!')
#            print('Count of records read : ', RescuerData.elements_count())
            print('Version of data: ', main_data.ver_no)
            print('E-mail my: ', main_data.email_my)
        except Exception as Id:
            print(f'Ошибка чтения файла options ({Id})')
            main_data = None

    if main_data is None:
        main_data = RescuerData('', '')
        main_data.elements_fill()
        main_data.print_dic()

        main_data.write_data()

#    print('Count of records written : ', len(main_data.elements))
# не работает совсем
    print('Count of records written : ', main_data.elements_count())
    print('E-mail my: ', main_data.email_my)
    print('E-mail your: ', main_data.email_your)

