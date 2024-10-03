from abc import ABC, abstractmethod


class GameObject():
    def __init__(self, id: int, name: str, x: int, y: int) -> None:
        self.id = id
        self.name = name
        self.x = x
        self.y = y

    @property
    def getId(self):
        return self.id

    @property
    def getName(self):
        return self.name

    @property
    def getX(self):
        return self.x

    @property
    def getY(self):
        return self.y


class Unit(GameObject):
    def __init__(self, id, name, x, y, hp) -> None:
        super().__init__(id, name, x, y)
        self.hp = hp

    @property
    def isAlive(self):
        return self.hp > 0

    @property
    def getHp(self):
        return self.hp

    def receiveDamage(self, damage):
        self.hp -= damage


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class Archer(Unit, Attacker, Moveable):
    def __init__(self, id, name, x, y, hp, attack_power):
        super().__init__(id, name, x, y, hp)
        self.attack_power = attack_power

    def attack(self, unit):
        if self.isAlive():
            unit.receiveDamage(self.attack_power)

    def move(self, x, y):
        self.x = x
        self.y = y


class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self.built = built

    @property
    def isBuilt(self):
        return self.built


class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, built, attack_power):
        super().__init__(id, name, x, y, built)
        self.attack_power = attack_power

    def attack(self, unit):
        if self.isBuilt():
            unit.receiveDamage(self.attack_power)


class MobileHouse(Building, Moveable):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y, built)

    def move(self, x, y):
        self.x = x
        self.y = y
