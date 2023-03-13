# pylint: disable-all
from collections import namedtuple

'''Same list with different elements'''

MyList = namedtuple("Purchase", "extra supermarkets local fruits")

def my_list():

    return MyList (
        fruits=["apple", "grape", "avocado"],
        local="street of orange trees",
        supermarkets=2,
        extras={"sweets": "chocolates", "juices": "strawberry"}
    )

def my_list2():

    return MyList (
        fruits=["Pear", "Banana"],
        local="Street of Orange Trees",
        supermarkets= 1,
        extras={"sweets": "chocolates"}
    )

lista = my_list()
lista2= my_list2()
print(list)
print(list2)
