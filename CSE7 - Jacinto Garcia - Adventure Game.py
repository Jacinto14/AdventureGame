import random
import sys

print("You are a young man named Bob, you have been enlisted in the army to fight for your country. Travel the world "
      "and discover new adventures. Do well.")
print()
print('For a list of commands type "help"')

commands = 'Remember to pick up weapons and equip them! (attack for combat, equip for weapons, consume, ' \
           'pick up, n, e, s, w to move)'


def combat(target):

    print("You have entered combat with %s" % target.name)
    print()
    print("You have %d health left." % Bob.health)
    print("%s has %d health left." % (target.name, target.health))
    while target.health > 0 and Bob.health > 0:

        move = input("> ")
        print()
        if move == 'equip':
            print("Enter the number of the item to equip it")
            for numb, equip in enumerate(Bob.bag):
                print(str(numb + 1) + ": " + equip.name)
            print()
            print()
            move = int(input('>')) - 1
            if Bob.bag[move].isweapon is True:
                Bob.defaultweapon = Bob.bag[move]
                print('You equip the item')
            elif Bob.bag[move].isweapon is not True:
                print('Item is not weapon')
        if move in ['help', 'ayuda']:
            print(commands)
            print()
        if move in ['q', 'quit', 'exit']:
            sys.exit(0)
        elif move in ['attack', 'hit', 'shoot']:
            Bob.attack(target)
            print("%s has %d health left." % (target.name, target.health))
            print()
            if target.isalive():
                target.attack(Bob)
                print("You have %d health left." % Bob.health)
                print()

    if Bob.health <= 0:
        print("GAME OVER")
        sys.exit(0)
    else:
        print("You defeat %s" % target.name)
        Bob.xp += 10
        print('You gain 10 xp points. You now have %s xp' % Bob.xp)
        Bob.levelup()
        if Tokyo.npc is None:
            print("You have brought peace to the world using %s, now you can live a normal life back home. "
                  % Bob.defaultweapon.name)


class Character(object):
    def __init__(self, name, health, dodamage, armor, bag=None, defaultweapon=None):
        if bag is None:
            bag = []
        self.dodamage = dodamage
        self.name = name
        self.health = health
        self.bag = bag
        self.armor = armor
        self.defaultweapon = defaultweapon

    def pick_up(self, items):
        self.bag.append(items)
        # print(self.bag)
        print()

    def attack(self, target):
        if target.health > 0:
            if self.defaultweapon is not None:
                self.defaultweapon.attack(target)
            else:
                print("%s is hit for %d damage." % (target.name, self.dodamage))
                target.take_damage(self.dodamage)

        else:
            print("%s now has %s health." % (target.name, target.health))

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health <= 0:
                print("%s has been slain" % self.name)
        else:
            print("%s is already dead" % self.name)

    def isalive(self):
        if self.health > 0:
            return True
        else:
            return False
            # 2


class Player(Character):
    def __init__(self, name, basehp, health, dodamage, armor, bag, defaultweapon, xp, money):
        super(Player, self).__init__(name, health, dodamage, armor, bag, defaultweapon)
        self.xp = xp
        self.basehp = basehp
        self.money = money

    def levelup(self):
        if self.xp > 50:
            self.health += 15
            self.xp = 0


class NPC(Character):
    def __init__(self, name, health, dodamage, armor, level):
        super(NPC, self).__init__(name, health, dodamage, armor)
        self.level = level


class Item(object):
    def __init__(self, name, value, isweapon):
        self.name = name
        self.value = value
        self.isweapon = isweapon

    def sell(self):
        print("You sell %s for %d sheckles." % (self.name, self.value))
        # Weapons

    def equip(self):
        Bob.defaultweapon = None
        if Bob.defaultweapon is None:
            Bob.defaultweapon = self
        print('You equip %s' % self.name)


# 3
class Weapon(Item):
    def __init__(self, name, value, damage, isweapon):
        super(Weapon, self).__init__(name, value, isweapon)
        self.damage = damage
        self.isweapon = True

    def attack(self, target):
        print('You attack %s for %d damage' % (target.name, self.damage))


# 4
class Gun(Weapon):
    def __init__(self, name, value, damage, ammo, isweapon):
        super(Gun, self).__init__(name, value, damage, isweapon)
        self.ammo = ammo

    def attack(self, target):
        if target.health > 0:
            if self.ammo > 0:
                self.ammo -= 1
                print("You shoot %s for %d damage." % (target.name, self.damage))
                target.health -= self.damage
                if self.ammo <= 0:
                    print("You run out of ammo.")
            else:
                print("Your gun does not have ammo.")
        else:
            print("%s does not have health." % target.name)


# 5
class Sniper(Gun):
    def __init__(self, name, value, damage, ammo, isweapon):
        super(Sniper, self).__init__(name, value, damage, ammo, isweapon)

    def attack(self, target):
        rand = random.randint(1, 10)
        if rand >= 8:
            if target.health > 0:
                    if self.ammo > 0:
                        self.ammo -= 1
                        print("You quickscope %s for %d damage." % (target.name, self.damage))
                        target.health -= self.damage
                        if self.ammo <= 0:
                            print("You run out of ammo.")
                    else:
                        print("Your gun does not have ammo.")
            else:
                print("%s does not have health." % target.name)
        else:
            print('Sorry, you missed your shot!')


# 6
class Dragunov(Gun):
    def __init__(self, name, value, damage, ammo, isweapon):
        super(Dragunov, self).__init__(name, value, damage, ammo, isweapon)

    def attack(self, target):
        if target.health > 0:
            if self.ammo > 0:
                self.ammo -= 1
                print("You spam %s for %d damage." % (target.name, self.damage))
                target.health -= self.damage
                if self.ammo <= 0:
                    print("You run out of ammo.")
            else:
                print("Your gun does not have ammo.")
        else:
            print("%s does not have health." % target.name)


# 7
class Knife(Weapon):
    def __init__(self, name, value, damage, durability, isweapon):
        super(Knife, self).__init__(name, value, damage, isweapon)
        self.durability = durability

    def attack(self, target):
        if self.durability > 0:
            print("You stab %s for %d damage." % (target.name, self.damage))
            target.health -= self.damage
            self.durability -= 2
            print("Your weapon now has %d durability left" % self.durability)
            if self.durability <= 0:
                print("Your weapon breaks.")
        else:
            print("Your weapon is broken.")
            # 8


class Switchblade(Knife):
    def __init__(self, name, value, damage, durability, isweapon):
        super(Switchblade, self).__init__(name, value, damage, durability, isweapon)
        self.durability = durability

    def attack(self, target):
        # if target.health > 0:
        if self.durability > 0:
            print("You stab %s for %d damage." % (target.name, self.damage))
            target.health -= self.damage
            self.durability -= 2
            print("Your switchblade now has %d durability left" % self.durability)
            if self.durability <= 0:
                print("Your switchblade breaks.")
        else:
            print("Your switchblade is broken.")
            # else:
            #  print '%s is dead' % target.name


# 9
class Bomb(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(Bomb, self).__init__(name, value, damage, isweapon)

    def attack(self, target):
        print("%s is blown up for %d damage." % (target.name, self.damage))
        target.health -= self.damage


# 10
class Flashbang(Weapon):
    def __init__(self, name, value, damage, duration, isweapon):
        super(Flashbang, self).__init__(name, value, damage, isweapon)
        self.duration = duration

    def attack(self, target):
        print("You flash %s for %d seconds." % (target.name, self.duration))


# 11
class NuclearBomb(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(NuclearBomb, self).__init__(name, value, damage, isweapon)

    def attack(self, target):
        if target.health >= 0:
            print("You end %s and humanity itself." % target.name)
            target.health -= self.damage
            if target.health <= 0:
                print("%s has been slain" % target.name)
        else:
            print("%s is already dead") % target.name


# 12
class Belt(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(Belt, self).__init__(name, value, damage, isweapon)

    def attack(self, target):
        print("You whip %s for %d damage." % (target.name, self.damage))
        target.health -= self.damage


# 13
class BrokenProtractor(Weapon):
    def __init__(self, name, value, damage, isweapon):
        super(BrokenProtractor, self).__init__(name, value, damage, isweapon)

    def attack(self, target):
        print("You geometrically stab %s for %d damage." % (target.name, self.damage))
        target.health -= self.damage

        # Vehicles


# 14
class Vehicle(Item):
    def __init__(self, name, value, speed, gas, isweapon):
        super(Vehicle, self).__init__(name, value, isweapon)
        self.speed = speed
        self.gas = gas
        self.isweapon = False

    def move(self):
        if self.gas > 0:
            print("You drive forward at %s miles per hour." % self.speed)
            self.gas -= 1
            print("You have %s gallons of gas left." % self.gas)
            if self.gas <= 0:
                print("You run out of gas.")
        else:
            print("Your vehicle has no gas left.")


# 15
class Tricycle(Item):
    def __init__(self, name, value, speed, isweapon):
        super(Tricycle, self).__init__(name, value, isweapon)
        self.speed = speed
        self.isweapon = False

    def move(self):
        print("You pedal forward at %s miles per hour." % self.speed)


# 16
class NitroTricycle(Tricycle):
    def __init__(self, name, value, speed, gas, isweapon):
        super(NitroTricycle, self).__init__(name, value, speed, isweapon)
        self.gas = gas

    def move(self):
        if self.gas > 0:
            print("You pedal furiously forward at %s miles per hour." % self.speed)
            self.gas -= 5
            print("You have %s gallons of gas left." % self.gas)
            if self.gas <= 0:
                print("You run out of gas.")
        else:
            print("Your plane doesn't have gas")


# 17
class Train(Vehicle):
    def __init__(self, name, value, speed, gas, isweapon):
        super(Train, self).__init__(name, value, speed, gas, isweapon)

    def move(self):
        if self.gas > 0:
            print("Your train choo choos forward at %s miles per hour." % self.speed)
            self.gas -= 2
            print("You have %s pounds of coal left." % self.gas)
            if self.gas <= 0:
                print("You run out of coal.")
        else:
            print("Your Train doesn't have gas")


# 18
class Plane(Vehicle):
    def __init__(self, name, value, speed, gas, isweapon):
        super(Plane, self).__init__(name, value, speed, gas, isweapon)

    def move(self):
        if self.gas > 0:
            print("Your plane flies forward at %s miles per hour." % self.speed)
            self.gas -= 1
            print("You have %s gallons of gas left." % self.gas)
            if self.gas <= 0:
                print("You run out of gas.")
        else:
            print("Your plane doesn't have gas")


# Consumable
# 19
class Consumable(Item):
    def __init__(self, name, value, uses, isweapon):
        super(Consumable, self).__init__(name, value, isweapon)
        self.uses = uses
        self.isweapon = False

    def consume(self, target, basehp):
        if self.uses > 0:
            print("%s consumes the item." % target.name)
            self.uses -= 1
            if target.health > basehp:
                target.health = basehp
            if self.uses <= 0:
                print("You run out of the item.")
        else:
            print('You no longer have that item')


# 20
class HealthKit(Consumable):
    def __init__(self, name, value, uses, health_regen, isweapon):
        super(HealthKit, self).__init__(name, value, uses, isweapon)
        self.health_regen = health_regen

    def consume(self, target, basehp):
        print("You consume the health kit.")
        self.uses -= 1
        target.health += self.health_regen
        if target.health > basehp:
            target.health = basehp
        if self.uses <= 0:
            print("You run out of the health kit.")


# 21
class Poison(Consumable):
    def __init__(self, name, value, uses, health_loss, isweapon):
        super(Poison, self).__init__(name, value, uses, isweapon)
        self.health_loss = health_loss

    def consume(self, target, basehp):
        if self.uses > 0:
            print("You consume the poison.")
            self.uses -= 1
            target.health -= self.health_loss

            print(target.health)
            if self.uses <= 0:
                print("You run out of the poison.")
        else:
            print('You no longer have any poison left.')


# 22
class ExpiredCandy(Consumable):
    def __init__(self, name, value, uses, health_loss, isweapon):
        super(ExpiredCandy, self).__init__(name, value, uses, isweapon)
        self.health_loss = health_loss

    def consume(self, target, basehp):
        if self.uses > 0:
            print("You consume the expired candy.")
            self.uses -= 1
            target.health -= self.health_loss
            print(target.health)
            if self.uses <= 0:
                print("You run out of the candy.")
        else:
            print('You no longer have any candy left.')


# 23
class Food(Consumable):
    def __init__(self, name, value, uses, health_regen, isweapon):
        super(Food, self).__init__(name, value, uses, isweapon)
        self.health_regen = health_regen

    def consume(self, target, basehp):
        if self.uses > 0:
            print("You consume the food.")
            self.uses -= 1
            target.health -= self.health_regen
            print("%s health left" % target.health)
            if self.uses <= 0:
                print("You run out of the food.")
        else:
            print('You no longer have any food left.')


# 24
class Armor(Item):
    def __init__(self, name, value, durability, defenseplus, isweapon):
        super(Armor, self).__init__(name, value, isweapon)
        self.durability = durability
        self.defenseplus = defenseplus
        self.isweapon = False

    def take_damage(self):
        if self.durability > 0:
            print("Your armor loses durability!")
            self.durability -= 1
            if self.durability <= 0:
                print("Your armor breaks!")
        else:
            print("Your armor is broken!")


# 25
class Tool(Item):
    def __init__(self, name, value, durability, isweapon):
        super(Tool, self).__init__(name, value, isweapon)
        self.durability = durability
        self.isweapon = False

    def usetool(self):
        if self.durability > 0:
            print("Your tool loses durability!")
            self.durability -= 1
            if self.durability <= 0:
                print("Your tool breaks!")
        else:
            print("Your tool is broken!")


# 26
class GrapplingHook(Tool):
    def __init__(self, name, value, durability, isweapon):
        super(GrapplingHook, self).__init__(name, value, durability, isweapon)

    def usetool(self):
        if self.durability > 0:
            print("Your %s loses durability!" % self.name)
            self.durability -= 1
            if self.durability <= 0:
                print("Your %s breaks!" % self.name)
        else:
            print("Your %s is broken!" % self.name)


# 27

class FishingRod(Tool):
    def __init__(self, name, value, durability, isweapon):
        super(FishingRod, self).__init__(name, value, durability, isweapon)

    def fish(self):
        rand = random.randint(1, 10)
        if rand >= 4:
            if self.durability > 0:
                print("You catch a fish")

                print("Your %s loses durability!" % self.name)
                self.durability -= 1
                if self.durability <= 0:
                    print("Your %s breaks!" % self.name)
            else:
                print("Your %s is broken!" % self.name)
        else:
            print("You do not catch a fish")
            print("Your %s loses durability!" % self.name)
            self.durability -= 1


# 28
class Wrench(Tool):
    def __init__(self, name, value, durability, isweapon):
        super(Wrench, self).__init__(name, value, durability, isweapon)

    def usetool(self):
        if self.durability > 0:
            print("You wrench a thing.")

            print("Your %s loses durability!" % self.name)
            self.durability -= 1
            if self.durability <= 0:
                print("Your %s breaks!" % self.name)
        else:
            print("Your %s is broken!" % self.name)


# 29
class Computer(Tool):
    def __init__(self, name, value, battery, isweapon, on=False):
        super(Computer, self).__init__(name, value, battery, isweapon)
        self.battery = battery
        self.on = on

    def turn_on(self):
        if self.on is True:
            print('Your computer is already on!')
        else:
            self.on = True
            print('You turn your computer on.')

    def use(self):
        if self.on is True:
            if self.battery > 0:
                print("You use your computer.")

                self.battery -= 1
                if self.battery <= 0:
                    print("Your computer is off!" % self.name)
        else:
            print("Your computer is off!")
            # 30


class Pencil(Tool):
    def __init__(self, name, value, durability, sharpness, isweapon):
        super(Pencil, self).__init__(name, value, durability, isweapon)
        self.durability = durability
        self.sharpness = sharpness

    def write(self):
        if self.sharpness >= 0:
            self.sharpness -= 1
            print("You write something somewhere")
            if self.sharpness == 0:
                print("Your pencil needs to be sharpened")
        else:
            print("Your pencil needs to be sharpened")


GermanSoldier1 = NPC('Charles M', 80, 20, None, 2)
GermanSoldier2 = NPC('Derek C', 80, 20, None, 2)
GermanSoldier3 = NPC('Abel N', 80, 20, None, 2)
GermanSoldier4 = NPC('George B', 100, 22, None, 2)
GermanSoldier5 = NPC('Zimmer M', 80, 20, None, 2)
GermanSoldier6 = NPC('Mister M', 80, 20, None, 2)
AustrianSoldier1 = NPC('Charles M', 80, 20, None, 2)

Lewis = Gun('Lewis Assault Rifle', 20, 10, 50, True)
Luger = Gun('Luger Pistol', 15, 20, 80, True)
Barrett = Sniper('Pedro\'s Barret', 50, 200, 10, True)
Drag = Dragunov('Dragunov', 20, 50, 50, True)
M1911 = Gun('M1911', 20, 30, 30, True)
Blade = Switchblade('Switchblade', 20, 10, 10, True)
Bomb = Bomb('Bomb', 20, 10, True)
Flash = Flashbang('FlashBang', 20, 19, 18, True)
Nuke = NuclearBomb('Nuke', 20, 1000, True)
Nuke2 = NuclearBomb('Nuke', 20, 1000, True)
Belt = Belt('My Belt', 20, 10, True)
Pro = BrokenProtractor('Broken Protractor', 20, 10, True)
Gewehr = Sniper('Fancy Gewehr', 15, 25, 15, True)
Dragg = Dragunov("Pedro's Dragunov", 20, 20, 20, True)
MachineGun = Gun('Vickers Machine Gun', 100, 70, 30, True)

Health = HealthKit('Healthkit', 20, 1, 100, False)
Health2 = HealthKit('Healthkit', 20, 1, 100, False)
Health3 = HealthKit('Healthkit', 20, 1, 100, False)
Health4 = HealthKit('Healthkit', 20, 1, 100, False)
Health5 = HealthKit('Healthkit', 20, 1, 100, False)
Waffle = Food('Waffle', 20, 1, 40, False)
Grapp = GrapplingHook('GrapplingHook', 40, 10, False)
Good_Fishing_Rod = FishingRod('FishingRod', 20, 1, False)

Wrench = Wrench('Wrench', 20, 1, False)
Key = Tool('Key', 5, 70, False)

Bob = Player('Bob', 150, 150, 10, 0, [Health], None, 0, 50)
Ronald = NPC('Ronald M', 80, 20, 20, 2)
Boss = NPC('German Boss Dude', 500, 50, 0, 10)


# World Map


class Room(object):
    def __init__(self, items, the_name, n, e, s, w, u, d, the_description, npc=None):
        self.name = the_name
        self.description = the_description
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.up = u
        self.down = d
        self.items = items
        self.npc = npc

    def move(self, direction):
        # This function allows movement to a different node.
        global node
        node = globals()[getattr(self, direction)]


class Shop(Room):
    def __init__(self, items, the_name, n, e, s, w, u, d, the_description, npc=None, buyable=None):
        super(Shop, self).__init__(items, the_name, n, e, s, w, u, d, the_description, npc)
        self.buyable = buyable
        if self.buyable is None:
            self.buyable = []

    def buy(self):
        print('You have %s sheckles' % Bob.money)
        print('----------------------------------------------------------------------------------------------')
        print('Type the number of the item of what you want to buy')
        print('Here is what you can buy: ')
        print('----------------------------------------------------------------------------------------------')
        for number, bought in enumerate(self.buyable):
            print(str(number + 1) + ": " + bought.name + " for %s sheckles" % bought.value)

        print()
        print()
        buy = int(input('>')) - 1
        if Bob.money >= Shopping.buyable[buy].value:
            Bob.money -= Shopping.buyable[buy].value
            Bob.pick_up(Shopping.buyable[buy])
            Shopping.buyable.pop(buy)
        else:
            print('You do not have enough money')
        print('You now have %s sheckles' % Bob.money)

# Rooms
Shopping = Shop([], 'Manchester, United Kingdom', None, None, 'London', None, None, None, 'Stay here and shop for '
                                                                                          'items!(Type "buy" to shop)',
                None, [Barrett, ])
London = Room([Luger, Health2], 'London, United Kingdom', 'Shopping', 'Liege', 'Paris', 'Ocean', None, None,
              'Industrial Center of the United Kingdom', None)
Liege = Room([Waffle], 'Liege, Belgium', None, 'Berlin', 'Switzerland', 'London', None, None,
             'There is a waffle store near you.', Ronald)
Washington = Room([Key], 'Washington DC', None, 'Ocean', None, 'Plato', None, None,
                  'Woodrow Wilson recently gave his inaugural speech, but the\
US has not entered the Great War yet', None)
Paris = Room([Bomb], 'Paris, France', 'London', None, None, 'Ocean', None, None,
             'You can see the eiffel tower', None)
Ocean = Room([Good_Fishing_Rod], 'The Pacific Ocean', None, 'Paris', None, 'Washington', None, None,
             '6,000 kilometers of blue water', None)
Switzerland = Room([Wrench], 'Switzerland', 'Liege', 'Sarajevo', 'Gallipoli', None, None, None,
                   'A completely neutral country, there is almost nothing to\
do here.', None)
Gallipoli = Room([Lewis], 'Gallipoli, Italy', 'Switzerland', 'Constantinople', None, None, None, None,
                 'The Central Powers have completely taken this area over.\
Watch your step!', None)

Constantinople = Room([Belt], 'Constantinople, Ottoman Empire', 'Moscow', None, None, 'Gallipoli', None, None,
                      'Capital of the Ottoman Empire, there are many people looking\
at you with a concerned face', None)
Sarajevo = Room([M1911], 'Sarajevo, Austria-Hungary', None, None, None, 'Switzerland', None, None,
                'The hearth of this brutal war.\
You can see Austro-Hungarian solders down the street.', None)
Moscow = Room([Health3], 'Moscow, Russian Empire', None, 'Maze', 'Constantinople', None, None, None,
              'Very cold. At least the Central Powers haven\'t \
invaded yet...', None)

Plato = Room([Blade], 'Plato, Missouri', None, 'Washington', None, 'Fresno', None, None,
             'The mean center of the US population', None)
Philadelphia = Room([Good_Fishing_Rod], 'Philadelphia, Pennsylvania', 'New_York', None, 'Washington', None, None,
                    None,
                    'You can smell the Liberty bell where you are standing, or\
it could be a cheesesteak...', None)
New_York = Room([MachineGun, Health4], 'New York, New York', None, None, 'Philadelphia', None, None, None,
                'Most populous US city.', None)
Fresno = Room([Nuke], 'Fresno, California', None, 'Plato', None, None, None, None,
              'Agricultural center. There is a small shack that you can see\
in the corner', GermanSoldier4)
Berlin = Room([Drag], 'Berlin, Germany', None, None, None, 'Liege', None, None,
              'Capital of the German Empire "Hallo!"', None)

Maze = Room([], 'Start of Confusing Tundra', 'Maze3', 'Maze2', None, 'Moscow', None, None,
            'It\'s cold and you don\'t know where to go.', None)
Maze2 = Room([], 'Confusing Tundra: This looks familiar...', 'Maze5', 'Maze4', None, 'Maze', None, None, None, None)
Maze3 = Room([], 'Confusing Tundra: This looks familiar...', None, None, 'Maze', None, None, None,
             'It\'s cold and you don\'t know where to go.', None)
Maze4 = Room([Gewehr], 'Confusing Tundra: This looks familiar...', None, 'Tokyo', None, 'Maze2', None, None,
             'It\'s cold and you don\'t know where to go.', GermanSoldier1)
Maze5 = Room([], 'Confusing Tundra: This looks familiar...', None, None, 'Maze2', None, None, None,
             'It\'s cold and you don\'t know where to go.', None)
Tokyo = Room([Nuke2], 'Tokyo', None, None, None, 'Maze4', None, None,
             'Soon to be nuked', Boss)

# static variables
# Controller
node = London
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
is_alive = True
Pickup = ['pick up']
while is_alive is True:
    if Tokyo.npc is None:
        print('-------------------------------------------------------------------------------------------')
        print("You have brought peace to the world using %s, now you can live a normal life back home. "
              % Bob.defaultweapon.name)
        print("-------------------------------------------------------------------------------------------")
        sys.exit(0)
    if node.npc is not None:
        combat(node.npc)
        node.npc = None
        print()
    print('----------------------------------------------------------------------------------------------------')
    print(node.name)
    print(node.description)
    print('----------------------------------------------------------------------------------------------------')
    print()
    print("You have the following items in your bag:")
    for item in Bob.bag:
        print(item.name)
    print()
    if len(node.items) > 0:
        print()
        print("There are following items(s):")
        for num, item in enumerate(node.items):
            print(str(num + 1) + ": " + item.name)
        print()
    # Ask for input

    command = input('> ')
    if command == 'buy':
        if node == Shopping:
            Shopping.buy()
    if command in ['q', 'quit', 'exit']:
        sys.exit(0)
    else:
        if command in Pickup:
            if len(node.items) > 0:
                print()
                print("Enter the number of the item to pick it up")
                for num, item in enumerate(node.items):
                    print(str(num + 1) + ": " + item.name)
                print()
                command = int(input('>')) - 1
                Bob.pick_up(node.items[command])
                node.items.pop(command)
        else:
            if command == 'equip':
                print("Enter the number of the item to equip it")
                for num, Weapon in enumerate(Bob.bag):
                    print(str(num + 1) + ": " + Weapon.name)
                print()
                print()
                command = int(input('>')) - 1
                if Bob.bag[command].isweapon is True:
                    Bob.defaultweapon = Bob.bag[command]
                    print(Bob.defaultweapon.name)
                elif Bob.bag[command].isweapon is not True:
                    print('Item is not weapon')
            else:
                if command == 'unequip':
                    Bob.defaultweapon = None

                else:
                    if command == 'consume':
                        print("Enter the number of the item to consume it")
                        for num, Consumable in enumerate(Bob.bag):
                            print(str(num + 1) + ": " + Consumable.name)
                        print()
                        print()
                        command = int(input('>')) - 1
                        Bob.bag[command].consume(Bob)
                        Bob.bag.pop(command)
                        if Bob.health > 150:
                            Bob.health = 150

                    else:
                        if command == 'help':
                            print(commands)
                            print()

                        # Allows us to change nodes

                        if command in short_directions:
                            command = directions[short_directions.index(command)]

                            # noinspection PyBroadException
                            try:
                                node.move(command)
                            except KeyError:
                                print("You can't!")
                            except AttributeError:
                                print("<PLACEHOLDER> Unknown Command.")
