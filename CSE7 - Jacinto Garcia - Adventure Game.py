import random
import sys
rand = random.randint(1, 10)


class Character(object):
    def __init__(self, name, health, dodamage, armor):
        self.dodamage = dodamage
        self.name = name
        self.health = health
        self.bag = ['Poison, Potion']
        self.armor = armor

    def pick_up(self, item):
        self.bag.append(str(item))
        print('You pick up the item')
        print(self.bag)

    def attack(self, target):

        print("%s is attacked for %d damage.") % (target.name, self.dodamage)
        target.take_damage(self.dodamage)

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            if self.health <= 0:
                print("%s has been slain")
        else:
            print("%s is already dead")
        print("You consume it")

        # 2


class Player(Character):
    def __init__(self, name, health, dodamage, armor, xp):
        super(Player, self).__init__(name, health, dodamage, armor)
        self.xp = xp


class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def sell(self):
        print("You sell %s for %d sheckles.") % (self.name, self.value)
        # Weapons


# 3
class Weapon(Item):
    def __init__(self, name, value, damage):
        super(Weapon, self).__init__(name, value)
        self.damage = damage

    def attack(self, target):
        print('You attack for %d damage') % self.damage


# 4
class Gun(Weapon):
    def __init__(self, name, value, damage, ammo):
        super(Gun, self).__init__(name, value, damage)
        self.ammo = ammo

    def attack(self, target):
        if target.health > 0:
            if self.ammo > 0:
                self.ammo -= 1
                print("You shoot %s for %d damage.") % (target.name, self.damage)
                target.health -= self.damage
                if self.ammo <= 0:
                    print("You run out of ammo.")
            else:
                print("Your gun does not have ammo.")
        else:
            print("%s does not have health.") % target.name


# 5
class Barret(Gun):
    def __init__(self, name, value, damage, ammo):
        super(Barret, self).__init__(name, value, damage, ammo)

    def attack(self, target):
        if target.health > 0:
            if self.ammo > 0:
                self.ammo -= 1
                print("You quickscope %s for %d damage.") % (target.name, self.damage)
                target.health -= self.damage
                if self.ammo <= 0:
                    print("You run out of ammo.")
            else:
                print("Your gun does not have ammo.")
        else:
            print("%s does not have health.") % target.name


# 6
class Dragunov(Gun):
    def __init__(self, name, value, damage, ammo):
        super(Dragunov, self).__init__(name, value, damage, ammo)

    def attack(self, target):
        if target.health > 0:
            if self.ammo > 0:
                self.ammo -= 1
                print("You spam %s for %d damage.") % (target.name, self.damage)
                target.health -= self.damage
                if self.ammo <= 0:
                    print("You run out of ammo.")
            else:
                print("Your gun does not have ammo.")
        else:
            print("%s does not have health.") % target.name


# 7
class Knife(Weapon):
    def __init__(self, name, value, damage, durability):
        super(Knife, self).__init__(name, value, damage)
        self.durability = durability

    def attack(self, target):
        if self.durability > 0:
            print("You stab %s for %d damage.") % (target.name, self.damage)
            target.health -= self.damage
            self.durability -= 2
            print("Your weapon now has %d durability left") % self.durability
            if self.durability <= 0:
                print("Your weapon breaks.")
        else:
            print("Your weapon is broken.")
            # 8


class Switchblade(Knife):
    def __init__(self, name, value, damage, durability):
        super(Switchblade, self).__init__(name, value, damage, durability)
        self.durability = durability

    def attack(self, target):
        # if target.health > 0:
        if self.durability > 0:
            print("You stab %s for %d damage.") % (target.name, self.damage)
            target.health -= self.damage
            self.durability -= 2
            print("Your switchblade now has %d durability left") % self.durability
            if self.durability <= 0:
                print("Your switchblade breaks.")
        else:
            print("Your switchblade is broken.")
            # else:
            #  print '%s is dead' % target.name


# 9
class Bomb(Weapon):
    def __init__(self, name, value, damage):
        super(Bomb, self).__init__(name, value, damage)

    def attack(self, target):
        print("%s is blown up for %d damage.") % (target.name, self.damage)
        target.health -= self.damage


# 10
class Flashbang(Weapon):
    def __init__(self, name, value, damage, duration):
        super(Flashbang, self).__init__(name, value, damage)
        self.duration = duration

    def attack(self, target):
        print("You flash %s for %d seconds.") % (target.name, self.duration)


# 11
class NuclearBomb(Weapon):
    def __init__(self, name, value, damage):
        super(NuclearBomb, self).__init__(name, value, damage)

    def attack(self, target):
        if target.health >= 0:
            print("You end %s and humanity itself.") % target.name
            target.health -= self.damage
            if target.health <= 0:
                print("%s has been slain") % target.name
        else:
            print("%s is already dead") % target.name


# 12
class Belt(Weapon):
    def __init__(self, name, value, damage):
        super(Belt, self).__init__(name, value, damage)

    def attack(self, target):
        print("You whip %s for %d damage.") % (target.name, self.damage)
        target.health -= self.damage


# 13
class BrokenProtractor(Weapon):
    def __init__(self, name, value, damage):
        super(BrokenProtractor, self).__init__(name, value, damage)

    def attack(self, target):
        print("You geometrically stab %s for %d damage.") % (target.name, self.damage)
        target.health -= self.damage

        # Vehicles


# 14
class Vehicle(Item):
    def __init__(self, name, value, speed, gas):
        super(Vehicle, self).__init__(name, value)
        self.speed = speed
        self.gas = gas

    def move(self):
        if self.gas > 0:
            print("You drive forward at %s miles per hour.") % self.speed
            self.gas -= 1
            print("You have %s gallons of gas left.") % self.gas
            if self.gas <= 0:
                print("You run out of gas.")
        else:
            print("Your vehicle has no gas left.")


# 15
class Tricycle(Item):
    def __init__(self, name, value, speed):
        super(Tricycle, self).__init__(name, value)
        self.speed = speed

    def move(self):
        print("You pedal forward at %s miles per hour.") % self.speed


# 16
class NitroTricycle(Tricycle):
    def __init__(self, name, value, speed, gas):
        super(NitroTricycle, self).__init__(name, value, speed)
        self.gas = gas

    def move(self):
        if self.gas > 0:
            print("You pedal furiously forward at %s miles per hour.") % self.speed
            self.gas -= 5
            print("You have %s gallons of gas left.") % self.gas
            if self.gas <= 0:
                print("You run out of gas.")
        else:
            print("Your plane doesn't have gas")


# 17
class Train(Vehicle):
    def __init__(self, name, value, speed, gas):
        super(Train, self).__init__(name, value, speed, gas)

    def move(self):
        if self.gas > 0:
            print("Your train choo choos forward at %s miles per hour.") % self.speed
            self.gas -= 2
            print("You have %s pounds of coal left.") % self.gas
            if self.gas <= 0:
                print("You run out of coal.")
        else:
            print("Your Train doesn't have gas")


# 18
class Plane(Vehicle):
    def __init__(self, name, value, speed, gas):
        super(Plane, self).__init__(name, value, speed, gas)

    def move(self):
        if self.gas > 0:
            print("Your plane flies forward at %s miles per hour.") % self.speed
            self.gas -= 1
            print("You have %s gallons of gas left.") % self.gas
            if self.gas <= 0:
                print("You run out of gas.")
        else:
            print("Your plane doesn't have gas")


# Consumable
# 19
class Consumable(Item):
    def __init__(self, name, value, uses):
        super(Consumable, self).__init__(name, value)
        self.uses = uses

    def consume(self, target):
        if self.uses > 0:
            print("You consume the item.")
            self.uses -= 1
            if self.uses <= 0:
                print("You run out of the item.")
        else:
            print('You no longer have that item')


# 20
class HealthKit(Consumable):
    def __init__(self, name, value, uses, health_regen):
        super(HealthKit, self).__init__(name, value, uses)
        self.health_regen = health_regen

    def consume(self, target):
        if self.uses > 0:
            print("You consume the health kit.")
            self.uses -= 1
            target.health += self.health_regen
            if self.uses <= 0:
                print("You run out of the health kit.")
        else:
            print('You no longer have any health kits left.')


# 21
class Poison(Consumable):
    def __init__(self, name, value, uses, health_loss):
        super(Poison, self).__init__(name, value, uses)
        self.health_loss = health_loss

    def consume(self, target):
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
    def __init__(self, name, value, uses, health_loss):
        super(ExpiredCandy, self).__init__(name, value, uses)
        self.health_loss = health_loss

    def consume(self, target):
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
    def __init__(self, name, value, uses, health_regen):
        super(Food, self).__init__(name, value, uses)
        self.health_regen = health_regen

    def consume(self, target):
        if self.uses > 0:
            print("You consume the food.")
            self.uses -= 1
            target.health -= self.health_regen
            print("%s health left") % target.health
            if self.uses <= 0:
                print("You run out of the food.")
        else:
            print('You no longer have any food left.')


# 24
class Armor(Item):
    def __init__(self, name, value, durability, defenseplus):
        super(Armor, self).__init__(name, value)
        self.durability = durability
        self.defenseplus = defenseplus

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
    def __init__(self, name, value, durability):
        super(Tool, self).__init__(name, value)
        self.durability = durability

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
    def __init__(self, name, value, durability):
        super(GrapplingHook, self).__init__(name, value, durability)

    def usetool(self):
        if self.durability > 0:
            print("Your %s loses durability!") % self.name
            self.durability -= 1
            if self.durability <= 0:
                print("Your %s breaks!") % self.name
        else:
            print("Your %s is broken!") % self.name


# 27

class FishingRod(Tool):
    def __init__(self, name, value, durability):
        super(FishingRod, self).__init__(name, value, durability)

    def fish(self):
        if rand >= 4:
            if self.durability > 0:
                print("You catch a fish")

                print("Your %s loses durability!") % self.name
                self.durability -= 1
                if self.durability <= 0:
                    print("Your %s breaks!") % self.name
            else:
                print("Your %s is broken!") % self.name
        else:
            print("You do not catch a fish")
            print("Your %s loses durability!") % self.name
            self.durability -= 1


# 28
class Wrench(Tool):
    def __init__(self, name, value, durability):
        super(Wrench, self).__init__(name, value, durability)

    def usetool(self):
        if self.durability > 0:
            print("You wrench a thing.")

            print("Your %s loses durability!") % self.name
            self.durability -= 1
            if self.durability <= 0:
                print("Your %s breaks!") % self.name
        else:
            print("Your %s is broken!") % self.name


# 29
class Computer(Tool):
    def __init__(self, name, value, battery, on=False):
        super(Computer, self).__init__(name, value, battery)
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
                    print("Your computer is off!") % self.name
        else:
            print("Your computer is off!")
            # 30


class Pencil(Tool):
    def __init__(self, name, value, durability, sharpness):
        super(Pencil, self).__init__(name, value, durability)
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


Bob = Character([''], 'Bob', 20, 20)
Ronald = Character([''], 'Ronald M', 20, 20)
Wep = Weapon('Generic Weapon', 20, 10)
Gunn = Gun('Generic Gun', 20, 34, 12)
Barrett = Barret('Pedro\'s Barret', 20, 19, 12)
Drag = Dragunov('Dragunov', 20, 11, 10)
Knife1 = Knife('Knife', 20, 10, 10)
Blade = Switchblade('Switchblade', 20, 10, 10)
Bomb = Bomb('Bomb', 20, 10)
Flash = Flashbang('FlashBang', 20, 19, 18)
Nuke = NuclearBomb('Nuke', 20, 10)
Belt = Belt('My Belt', 20, 10)
Pro = BrokenProtractor('Broken Protractor', 20, 10)
Vehicle1 = Vehicle('Generic Vehicle', 20, 10, 10)
Tri = Tricycle('Tricycle', 20, 10)
Nitro1 = NitroTricycle('Nitro', 20, 10, 10)
test = Vehicle("test", 100, 1, 1)
Train = Train('Ay', 20, 1, 1)
Plane = Plane('Ay', 20, 1, 1)
Consumable1 = Consumable('Ay', 20, 1)
Health = HealthKit('Ay', 20, 1, 1)
Posion = Poison('Ay', 20, 1, 2)
Expired = ExpiredCandy('Ay', 20, 2, 2)
Waffle = Food('Waffle', 20, 1, 2)
Armor = Armor('Ay', 20, 1, 1)
Tool1 = Tool('Ay', 20, 1)
Grapp = GrapplingHook('Ay', 20, 1)
Good_Fishing_Rod = FishingRod('Ay', 20, 1)
Wrench = Wrench('Ay', 20, 1)
OldComputer = Computer('Ay', 20, 1, False)
Pencil = Pencil('Ay', 20, 1, 1)


# World Map

class Room(object):
    def __init__(self, items, the_name, n, e, s, w, u, d, the_description):
        self.name = the_name
        self.description = the_description
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.up = u
        self.down = d
        self.items = items

    def move(self, direction):
        # This function allows movement to a different node.
        global node
        node = globals()[getattr(self, direction)]

# Rooms
London = Room(['M1911', 'Pencil'], 'London, United Kingdom', None, 'Liege', 'Paris', 'Ocean', None, None,
              'Industrial Center of the United Kingdom')
Liege = Room(['Waffle'], 'Liege, Belgium', None, 'Berlin', 'Switzerland', 'London', None, None,
             'There is a waffle store near you.')
Washington = Room(['OldComputer'], 'Washington DC', None, 'Ocean', None, 'Plato', None, None,
                  'Woodrow Wilson recently gave his inaugural speech, but the\
US hasn\'t entered the Great War yet')
Paris = Room(['Bomb'], 'Paris, France', 'London', None, None, 'Ocean', None, None,
             'You can see the eiffel tower')
Ocean = Room(['Good_Fishing_Rod'], 'The Pacific Ocean', None, 'Paris', None, 'Washington', None, None,
             '6,000 kilometers of blue water')
Switzerland = Room(['Wrench'], 'Switzerland', 'Liege', 'Sarajevo', 'Gallipoli', None, None, None,
                   'A completely neutral country, there is almost nothing to\
do here.')
Gallipoli = Room(['Gunn'], 'Gallipoli, Italy', 'Switzerland', 'Constantinople', None, None, None, None,
                 'The Central Powers have completely taken this area over.\
 Watch your step!')

Constantinople = Room(['Belt'], 'Constantinople, Ottoman Empire', 'Moscow', None, None, 'Gallipoli', None, None,
                      'Capital of the Ottoman Empire, there are many people looking\
 at you with a concerned face')
Sarajevo = Room(['Posion'], 'Sarajevo, Austria-Hungary', None, None, None, 'Switzerland', None, None,
                'The hearth of this brutal war.\
 You can see Austro-Hungarian solders down the street.')
Moscow = Room(['Belt'], 'Moscow, Russian Empire', None, 'Maze', 'Constantinople', None, None, None,
              'Very cold. Atleast the Central Powers haven\'t \
 invaded yet...')

Plato = Room(['Blade'], 'Plato, Missouri', None, 'Washington', None, 'Fresno', None, None,
             'The mean center of the US population')
Philadelphia = Room(['Good_Fishing_Rod'], 'Philadelphia, Pennsylvania', 'New_York', None, 'Washington', None, None,
                    None,
                    'You can smell the Liberty bell where you are standing, or\
 it could be a cheesesteak...')
New_York = Room(['Blade'], 'New York, New York', None, None, 'Philadelphia', None, None, None,
                'Most populous US city.')
Fresno = Room(['Nuke'], 'Fresno, California', None, 'Plato', None, None, None, None,
              'Agricultural center. There is a small shack that you can see\
in the corner')
Berlin = Room(['Drag'], 'Berlin, Germany', None, None, None, 'Liege', None, None,
              'Capital of the German Empire "Hallo!"')

Maze = Room([''], 'Start of Confusing Tundra', 'Maze3', 'Maze2', None, 'Moscow', None, None,
            'It\'s cold and you don\'t know where to go.')
Maze2 = Room([''], 'Confusing Tundra: This looks familiar...', 'Maze5', 'Maze4', None, 'Maze', None, None,
             'Your starting point')
Maze3 = Room([''], 'Confusing Tundra: This looks familiar...', None, None, 'Maze', None, None, None,
             'It\'s cold and you don\'t know where to go.')
Maze4 = Room([''], 'Confusing Tundra: This looks familiar...', None, 'Tokyo', None, 'Maze2', None, None,
             'It\'s cold and you don\'t know where to go.')
Maze5 = Room([''], 'Confusing Tundra: This looks familiar...', None, None, 'Maze2', None, None, None,
             'It\'s cold and you don\'t know where to go.')
Hiroshima = Room(['Nuke'], 'Hiroshima', None, None, None, 'Maze4', None, None,
                 'Soon to be nuked')

Bob.pick_up('Pencil')


# static variables
# Controller
node = London
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
is_alive = True
actions = []
Attacking = ['hit', 'attack', 'shoot']
Enemies = ['Ronald']
Pickup = ['pick up']

while is_alive is True:
    print(node.name)
    print(node.description)
    print(node.items)
    # Ask for input
    command = input('> ')
    if command in ['q', 'quit', 'exit']:
        sys.exit(0)
    else:
        if command in Pickup:
            print('Pick up what?')
            pickup = input('>')
            if pickup in node.items:
                Bob.pick_up(pickup)
                listindex = node.items.index(pickup)
                node.items.pop(listindex)
                print(node.items)
        else:
            if command in Attacking:
                print('Attack who?')
                who = input('> ')

            else:
                # Allows us to change nodes
                if command in short_directions:
                    command = directions[short_directions.index(command)]

                # noinspection PyBroadException
                try:
                    node.move(command)
                except:
                    print('You can\'t')
