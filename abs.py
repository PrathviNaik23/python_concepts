from abstraction import Fan

class Cieling_fan(Fan):

    def turn_on(self):
        print("fan turned on")

    def change_speed(self, new_speed):
        print(f"Speed change from {self.current_speed} to {new_speed}") 

    def turn_off(self):
        print("fan turned off")   

obj =Cieling_fan(2,4)
obj.turn_on()
obj.motor()
obj.change_speed(4)
obj.turn_off()            