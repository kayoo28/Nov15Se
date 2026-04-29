class Parent:
    def show(self):
        print("This is Parent method")

class Child(Parent):
    def show(self):
        print("This is Child method (Overridden)")

obj = Child()
obj.show()