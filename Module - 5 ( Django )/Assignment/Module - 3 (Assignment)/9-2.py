class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def own(self):
        print("Child: Coding")

obj = Child()
obj.skills()   
obj.own()