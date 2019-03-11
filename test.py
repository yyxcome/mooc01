'''
这是一个面向对象的代码，定义两个类，一个人类，一个狗类，然后人够互动
'''
class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 每一个角色都有自己的昵称;
        self.aggressivity = aggressivity  # 每一个角色都有自己的攻击力;
        self.life_value = life_value  # 每一个角色都有自己的生命值;

    def attack(self,dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.aggressivity
egg = Person('egon',10,1000)

class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性都是狗

    def __init__(self, name, breed, aggressivity, life_value):
        self.name = name  # 每一只狗都有自己的昵称;
        self.breed = breed  # 每一只狗都有自己的品种;
        self.aggressivity = aggressivity  # 每一只狗都有自己的攻击力;
        self.life_value = life_value  # 每一只狗都有自己的生命值;

    def bite(self, people):
        Dog.life_value -= self.aggressivit
        # 狗可以咬人，这里的狗也是一个对象。
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
ha2 = Dog('二愣子','哈士奇',10,1000)  #创造了一只实实在在的狗ha2
print(ha2.life_value)         #看看ha2的生命值
egg.attack(ha2)               #egg打了ha2一下
print(ha2.life_value)         #ha2掉了10点血