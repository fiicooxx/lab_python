class Turtle:
    def __init__(self, name, speed):
    # inicjalizacja: pola name i speed z konstruktora, pole prywatne __x określające położenie, na starcie = 0
        self.name = name
        self.speed = speed
        self.__x = 0
    
    def say_name(self):
    # printer, przedstaw żółwia i powiedz jaką ma szybkość
        print(f"Hello I'm a turtle. My name is {self.name} and I travel with a speed of {self.speed} :D.")
    
    def move(self, distance):
    # zmień wartość położenia o distance
        self.__x += distance
    
    def get_position(self):
    # zwróć położenie
        return self.__x
    
def main():
    turtle1 = Turtle(name="Turtlik", speed=5)
    turtle1.say_name() 
    turtle1.move(10)
    print(turtle1.get_position())
    turtle1.move(10)
    turtle1.move(15)
    print(turtle1.get_position())

main()