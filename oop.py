import datetime


class Person:
    def __init__(self, name: str, weight: float = 0, birthday: datetime.datetime = None):
        self.name = name.title()
        self.person_birth_weight = weight
        self.birthday = birthday or datetime.datetime.now()

    def run(self):
        print(f' {self.name}is running...')



person1 = Person(name='alex', weight=3.600, birthday=datetime.datetime(year=1980, month=4, day=10))
person2 = Person(name='Donald', weight=4.2)

# print(person1.name)
# person2.run()
# person1.run()
# print(person1.birthday)
#
# print(person1)
# print(person2)
# print(person1 == person2)
