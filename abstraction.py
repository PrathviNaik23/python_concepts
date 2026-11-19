from abc import ABC,abstractmethod

class Fan(ABC):

    min_speed = 1
    max_speed = 5

    def __init__(self,current_speed,blade):
        self.current_speed = current_speed
        self.blade = blade

    @abstractmethod
    def turn_on(self):
        pass

    def motor(self):
        print("motor start rotating")

    @abstractmethod
    def change_speed(self,new_speed):
        pass

    @abstractmethod
    def turn_off(self):
        pass
    


