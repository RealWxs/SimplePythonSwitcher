from delegator import Delegator


delegator = Delegator()


@delegator.delegate(1)
def handleFunc1():
    print("handleFunc1")

@delegator.delegate(2)
def handleFunc2(arg):
    print("handleFunc2, arg: {}".format(arg))

@delegator.default
def defaultHandler():
    print("defaultHandler")


if __name__ == "__main__":
    delegator.switch(1)
    delegator.switch(2, "hello")
    delegator.switch(3)
    