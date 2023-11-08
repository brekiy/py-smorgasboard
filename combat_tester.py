import random

# unit combat tester for tbs game
class Weapon:
    def __init__(self, name: str, accuracy: int, pierce: int, damage: int, shots: int):
        self.name = name
        self.accuracy = accuracy
        self.pierce = pierce
        self.shots = shots
        self.damage = damage
        
class Unit:
    def __init__(self, name: str, hp: int, armor: int, weapon: Weapon):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
    
    def __repr__(self) -> str:
        return f"{self.name}: {self.hp} HP, carrying {self.weapon.name}"

class Squad:
    def __init__(self, members: list):
        self.members = members

    def shoot_target(self, target):
        # queue up all shots from each member, assign popped shots to a random member of the target squad
        # should the game have simultaneous attacks? or just switch between sides moving a single unit
        print("target pre attack", target.members)
        squad_attacks = {}
        for member in self.members:
            squad_attacks[member.name] = {
                "shots_remaining": member.weapon.shots
            }

        while squad_attacks and target.members:
            name = random.choice(list(squad_attacks.keys()))
            squad_attacks[name]["shots_remaining"] -= 1
            if squad_attacks[name]["shots_remaining"] <= 0:
                squad_attacks.pop(name)
            
            attacker = None
            for i in self.members:
                if i.name == name:
                    attacker = i
            target_member = random.choice(target.members)

            if random.randrange(1, 100) <= attacker.weapon.accuracy:
                target_member.hp -= attacker.weapon.damage - max(target_member.armor - attacker.weapon.pierce, 0)
                if target_member.hp <= 0:
                    print(f"{target_member.name} has been shot and killed by {attacker.name}'s {attacker.weapon.name}")
                    target.members.remove(target_member)
                else:
                    print(f"{target_member.name} has been shot by {attacker.name}'s {attacker.weapon.name}")
            else:
                print(f"{target_member.name} has been shot at by {attacker.name}'s {attacker.weapon.name} but it missed")

        print("target post attack", target.members)

if __name__ == "__main__":
    plasma = Weapon("plasma", 50, 15, 25, 1)
    bolter = Weapon("bolter", 35, 5, 10, 5)
    squad1 = Squad([Unit("a", 30, 7, bolter), Unit("b", 30, 7, bolter), Unit("c", 30, 7, bolter), Unit("d", 30, 7, bolter), Unit("e", 30, 7, plasma)])
    squad2 = Squad([Unit("f", 30, 7, bolter), Unit("g", 30, 7, bolter), Unit("h", 30, 7, bolter), Unit("i", 30, 7, bolter), Unit("j", 30, 7, plasma)])
    # squad1.shoot_target(squad2)
    # squad2.shoot_target(squad1)