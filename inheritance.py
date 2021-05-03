# very important concept in OOP
# very useful in classes and objects
class Parent:
    def your_last_name(self):
        print("roberts")


class Child(Parent):

    def your_first_name(self):
        print("bucky")

    def your_last_name(self):   # if this function is not over riden then the 16th line would print roberts
        print("green")


r = Child()
r.your_first_name()
r.your_last_name()
r.your_last_name()
