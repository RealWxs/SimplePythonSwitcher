from delegator import Delegator

delegator = Delegator()

@delegator.delegate('drink')
def drink(juice):
    print(f"drink {juice}")

@delegator.delegate(2)
def eat(food, dessert):
    print(f"eat {food} and {dessert}")

@delegator.default
def sleep():
    print("sleeping")


if __name__ == "__main__":
    delegator.switch("drink", "apple juice")
    delegator.switch(2, food="pizza", dessert="ice cream")
    delegator.switch(None)
    delegator.dispatch("drink")("orange juice")
    