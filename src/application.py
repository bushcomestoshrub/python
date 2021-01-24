from model.person import Person
from tmp.Tmp import asdf as my_string

print(my_string)


def hello():
    return "Hi there"


def good_bye():
    return "Adios"


if __name__ == "__main__":
    p = Person("Bob")
    print(f'{hello()} {p.name}')






