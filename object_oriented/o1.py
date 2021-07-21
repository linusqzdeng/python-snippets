# -*- coding: UTF-8 -*-

class Roommate():
    roommate1 = 'Fatty'
    roommate2 = 'Kase'
    roommate3 = 'Queena'
    me = 'Linus'

    name = 'Yo'       # 类变量
    age = 100
    sum = 0
    multiple = 2

    def __init__(self, name, age):
        self.name = name        # 实例变量
        self.age = age
        # print(name)
        # print(age)

        self.__class__.sum += 1
        print('The number of the roommates is:', self.__class__.sum)

    def chef_of_the_day(self):
        print('Monday:', self.roommate1)
        print('Tuesday:', self.roommate2)
        print('Wednesday:', self.roommate3)
        print('Thursday:', self.me)

    @classmethod        # 类方法
    def cal_plus(cls):
        cls.sum *= 2
        print(cls.sum)


roommate1 = Roommate('Queena', 23)
Roommate.cal_plus()
roommate2 = Roommate('Fatty', 22)
Roommate.cal_plus()
roommate3 = Roommate('Kase', 22)
Roommate.cal_plus()
