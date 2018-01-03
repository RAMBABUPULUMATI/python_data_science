class Student:

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.' + last + '@school.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.marks = int(self.marks*1.05)

class Dumb (Student):

    pass


Std_1 = Dumb('neel', 'verma', 60)

print(Std_1.email)

