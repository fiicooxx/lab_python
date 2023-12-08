import random

class Employee:
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Employee {self.name} (ID: {self.id}), position: {self.position}, salary: ${self.salary}")

    def promote(self, new_position):
        print(f"{self.name} has been promoted to {new_position}.")
        self.position = new_position

    def give_raise(self, amount):
        print(f"{self.name} has received a salary raise of ${amount}.")
        self.salary += amount

class Monster:
    def __init__(self, name, lvl, health, attack_damage, location):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.attack_damage = attack_damage
        self.location = location

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. [Health: {self.health}]")
        if (self.health) <= 0:
            self.die()

    def attack(self, target):
        print(f"{self.name} has attacked {target} for {self.attack_damage} damage")

    def die(self):
        print(f"{self.name} has been defeated!")
        loot = self.generate_loot()
        print(f"Loot: {loot}")
        
    def generate_loot(self):
        loot_table = {
            1: ["Health Potion", "10 x Silver credits"],
            2: ["Magic Silver Ring", "2 x Gold Coin"],
            3: ["Epic Axe", "Rare Armor"]
        }

        loot_level = min(self.lvl, max(loot_table.keys()))

        loot = random.choice(loot_table[loot_level])

        return loot
    
    def display_info(self):
        print(f'''
            ### {self.name} ###
            LVL: {self.lvl}
            HEALTH: {self.health}
            ATTACK DAMAGE: {self. attack_damage}
            LOCATION: {self.location}
        ''')
    
class Refrigerator:
    def __init__(self, brand, capacity, temperature):
        self.brand = brand
        self.capacity = capacity  
        self.temperature = temperature 
        self.contents = []  

    def cool_down(self):
        print(f"{self.brand} refrigerator is cooling down.")
        self.temperature -= 2

    def store_food(self, food_item):
        print(f"Storing {food_item} in the {self.brand} refrigerator.")
        self.contents.append(food_item)

    def remove_food(self, food_item):
        if food_item in self.contents:
            print(f"Removing {food_item} from the {self.brand} refrigerator.")
            self.contents.remove(food_item)
        else:
            print(f"{food_item} not found in the {self.brand} refrigerator.")

    def display_contents(self):
        print(f'''
            === {self.brand} Refrigerator Contents ===
            Temperature: {self.temperature}°C
            Capacity: {self.capacity} liters
            Contents: {', '.join(self.contents)}
        ''')

def main():
    # Employee
    employee1 = Employee(id=1, name="John Doe", position="Software Engineer", salary=14000)
    employee1.display_info()

    employee1.promote("Senior Software Engineer")
    employee1.give_raise(10000)

    employee1.display_info()

    # Monster
    monster1 = Monster(name="Basilisk", lvl=3, health=50, attack_damage=25, location = "Caves, Cellars")
    monster1.display_info()
    monster1.attack("Player 1")
    monster1.take_damage(20)
    monster1.attack("Player 2")
    monster1.take_damage(45)

    # Ref
    fridge1 = Refrigerator(brand="Samsung", capacity=500, temperature=4)
    fridge1.cool_down()
    fridge1.store_food("Milk")
    fridge1.store_food("Eggs")
    fridge1.display_contents()

    fridge1.remove_food("Juice")
    fridge1.remove_food("Milk")
    fridge1.display_contents()
    
main()