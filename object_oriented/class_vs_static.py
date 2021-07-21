class FirstName:
    def __init__(self, first_name):
        self.first_name = first_name

    def capitaliser(self):
        print(self.first_name.capitalize())


class LastName(FirstName):


bro_1 = FirstName('linus')
bro_1.capitaliser()
