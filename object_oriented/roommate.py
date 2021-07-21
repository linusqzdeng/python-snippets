import datetime

class Roommate:

    num_of_roommates = 0
    bonus_ratio = 1.5

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@abdn.ac.uk'

        Roommate.num_of_roommates += 1

    # magic methods
    def __add__(self, other):
        return self.salary + other.salary

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def mate_earned(self):
        self.salary = self.bonus_ratio * self.salary

    @classmethod
    def set_bonus(cls, bonus):
        cls.bonus_ratio = bonus

    @classmethod        # classmethod used as a constructor
    def from_string(cls, roommate_string):
        first, last, salary = roommate_string.split('-')
        return cls(first, last, salary)

    @staticmethod       # use static method when the function has nothing to do with the instance
    def is_school(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Classmate(Roommate):

    bonus_ratio = 1.2

    def __init__(self, first, last, salary, height):
        super().__init__(first, last, salary)
        self.height = height


class Lecturer(Roommate):

    def __init__(self, first, last, salary, stu=None):
        super().__init__(first, last, salary)
        if stu is None:
            self.stu = []
        else:
            self.stu = stu

    def add_stu(self, stu):
        if stu not in self.stu:
            self.stu.append(stu)

    def remove_stu(self, stu):
        if stu in self.stu:
            self.stu.remove(stu)

    def print_stu(self):
        for stu in self.stu:
            print("--->", stu.fullname())


mate_1 = Roommate('qizhong', 'deng', 500)
mate_2 = Roommate('xuecong', 'chen', 99999)

# print(Roommate.fullname(mate_1))
# print(mate_2.fullname())
# Roommate.mate_earned(mate_1)
# print(mate_1.email)
# print(mate_1.salary)

# Roommate.set_bonus(1.8)     # reset the bonus ratio by using classmethod
# print(mate_1.bonus_ratio)
# print(mate_2.bonus_ratio)

# roommate_string_3 = 'qiannan-xu-99999'
# roommate_string_4 = 'kaihan-yao-88888'

# mate_3 = Roommate.from_string(roommate_string_3)
# mate_4 = Roommate.from_string(roommate_string_4)

# print(Roommate.fullname(mate_3))
# print(mate_3.email)

# check_date = datetime.date(2021, 5, 11)

# print(Roommate.is_school(check_date))
# print(Roommate.num_of_roommates)


# classmate_1 = Classmate('yanxun', 'shi', 45678, 165)
# print(classmate_1.first, classmate_1.email, classmate_1.height)

# lecturer_1 = Lecturer('martin', 'wersing', 999999, [classmate_1, mate_1, mate_2])
# print(lecturer_1.print_stu())
# lecturer_1.remove_stu(classmate_1)
# print(lecturer_1.print_stu())

print(mate_1.__add__(mate_2))
