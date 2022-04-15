from dataclasses import dataclass
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

@dataclass(frozen=True)
class Person:
    name : str
    age : int
    weight: float

    def withName(self, name):
        return Person(name, self.age, self.weight)

    def withAge(self, age):
        return Person(self.name, age, self.weight)


    def withWeight(self, weight):
        return Person(self.name, self.age, weight)


person1 = Person("Lucy", 10, 50)
person1 = person1.withName("Himeko").withAge(28)
person_serialized = MyEncoder().encode(person1)
print(person_serialized)







