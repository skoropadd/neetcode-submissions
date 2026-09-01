class Hero:
    def __init__(self, name: str, power: int, health = 100):
        self.name = name
        self.power = power
        self.health = health
    
    def attack(self) -> int:
        return self.power

# TODO: Implement the Warrior and Mage classes
class Warrior(Hero):
    def attack(self) -> int:
        return self.power + 10 

class Mage(Hero):
    def __init__(self, name, power):
        super().__init__(name, power, health = 80)

    def attack(self):
        return self.power + 20 

# TODO: Implement the battle function
def show_attack(hero):
    print(f'{hero.name} attacks with {hero.attack()} damage!')



# Do not modify the following code
warrior = Warrior("Bob", 20)
mage = Mage("Alice", 15)

show_attack(warrior)  
show_attack(mage)    
