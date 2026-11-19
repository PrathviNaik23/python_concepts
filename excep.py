class NameIncorrectError(Exception):
    pass

class Validate_Name:

    def __init__(self,name):
        self.name = name

    def check_name(self):
        for i in self.name:
            if not (('A'<=i <='Z') or ('a'<= i <='z')):
                raise NameIncorrectError("Name should only contian alphabet")
        
user_name = input("Enter name: ")
obj = Validate_Name(user_name)
try:
    obj.check_name()
except NameIncorrectError as e:
    print(e)
else:
    print("Valid Name")        
                