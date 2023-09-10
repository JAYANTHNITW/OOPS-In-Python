class Human(object):
  def __int__(self,name,age):
    print("calling init from human class")
    self.Name = name
    self.Age = age
  def eat(self):
    print("I can eat")

class Male(Human):
  
  def sleep(self):
    print("I can sleep whole day")

class Female(Human):
  def __init__(self,name,age,can_dance) -> None:
    super().__init__(name,age)
    self.knowing_dancing = can_dance
  def work(self):
    print("I can work")
 
male_1 = Male()
male_1.sleep()
female_1 = Female(can_dance="yes")
female_1.eat()

