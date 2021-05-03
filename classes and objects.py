class Enemy:
    life = 3

    def attack(self):  # while using variable inside a class, self should be used
        print("ouch!")
        self.life -= 1

    def check_enemy_life(self):
        if self.life <= 0:
            print("i am dead")
        else:
            print(str(self.life) + ' life left')


enemy1 = Enemy()
enemy2 = Enemy()
enemy1.attack()
enemy1.attack()
enemy1.check_enemy_life()
enemy2.check_enemy_life()
# enemy1 is attacked and life is decreased but it doesnot affect enemy2
# this is the main advantage of classes and objects
# this concept is used in making games

# concept of init
# init is any function which is called automatically when you create an object. you donot have to call it explicitly


class Tuna:
    def __init__(self,x):
        self.energy = x

    def energy_level(self):
        print(self.energy)


enemy1 = Tuna(3)
enemy2 = Tuna(17)
enemy1.energy_level()
enemy2.energy_level()

# class variable and instance variable


class Girl:
    gender = "female"   # gender is the class variable, it is always same for any object created from this class

    def __init__(self,name):        # name is the instance variable and it is unique to each object or each girl
        self.intro = name


r = Girl('Rachel')
s = Girl('stanky')
print(r.gender)
print(s.gender)
print(r.intro)
print(s.intro)


