class CMS:
    def __init__(self,password):
        self.__password = password

    #getter method
    def get_pw(self):
        return self.__password

    #setter method
    def set_pw(self,new_password):
        if len(new_password)==8:
            self.__password=new_password
        else:
            print("keep exactly 8")

    # var = property(get_pw,set_pw)

obj1 = CMS("lion") 
# print(obj1.get_pw())
obj1.set_pw("king@123")
# print(obj1.var) 
print(obj1.get_pw())

