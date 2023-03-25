from delegator import Delegator

delegator = Delegator()


# argument is the case name in the switch
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
    # in switch, first argument is the variable to be switched, others is argument the target function need     
    delegator.switch(2, food="pizza", dessert="ice cream")
    delegator.switch(None)
    # in dispatch, return value is the function to be executed, and you can pass the argument like you're just using that function      
    delegator.dispatch("drink")("orange juice")
    
