class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

class Bird(Animal):
    def __init__(self, species, sound, wingspan):
        super().__init__(species, sound)
        self.wingspan = wingspan

    def fly(self):
        print(f"The {self.species} is flying with a wingspan of {self.wingspan} inches.")

class Parrot(Bird):
    def __init__(self, species, sound, wingspan, color):
        super().__init__(species, sound, wingspan)
        self.color = color

    def mimic_human(self):
        print(f"The {self.color} parrot mimics human speech.")
        
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        print(f"{self.name} attacks {target} for {self.attack_power} damage.")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

class Warrior(Character):
    def __init__(self, name, health, attack_power, weapon_type):
        super().__init__(name, health, attack_power)
        self.weapon_type = weapon_type

    def use_special_attack(self):
        print(f"{self.name} uses a special attack with their {self.weapon_type}.")

class Wizard(Character):
    def __init__(self, name, health, attack_power, magic_power):
        super().__init__(name, health, attack_power)
        self.magic_power = magic_power

    def cast_spell(self, target):
        print(f"{self.name} casts a spell on {target} using {self.magic_power} magic power.")
        
def main():
    animal1 = Animal(species="Unknown", sound="mysterious")
    animal1.make_sound()

    bird1 = Bird(species="Eagle", sound="screech", wingspan=72)
    bird1.make_sound()
    bird1.fly()

    parrot1 = Parrot(species="African Grey", sound="squawk", wingspan=18, color="grey")
    parrot1.make_sound()
    parrot1.fly()
    parrot1.mimic_human()

    player1 = Character(name="Player 1", health=100, attack_power=20)
    player1.attack("Enemy 1")

    warrior1 = Warrior(name="Warrior 1", health=150, attack_power=25, weapon_type="Sword")
    warrior1.attack("Enemy 2")
    warrior1.use_special_attack()

    wizard1 = Wizard(name="Wizard 1", health=120, attack_power=18, magic_power="Fireball")
    wizard1.attack("Enemy 3")
    wizard1.cast_spell("Enemy 3")

main()