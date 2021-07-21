# Using @property decorator can get access to an instance as an attribute
# No meed to use the bracket to call the function

class Roommate:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@abdn.ac.uk".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


mate_1 = Roommate("kaihan", "yo")
mate_2 = Roommate("qiannan", "xu")

mate_1.fullname = 'xuecong chen'

print(mate_1.email)
print(mate_1.fullname)
