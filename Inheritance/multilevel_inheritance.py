class Grandfather:
    def __init__(self):
        self.nose_size='big'
        self.angery='very anger'
    def health(self):
        print('not good')

    def sleep(self):
        print('sleep of 10 hours a day')

    def work(self):
        print('worked very hard since childhood')

class Father(Grandfather):
    def __init__(self):
        self.nose_size='not so big'
        self.angery = 'very anger than him'

    def health(self):
        print('good and okay')

    def work(self):
        print('He is also working hard')


class Son(Father):
    def excercise(self):
        print('daily workout for 30 min')
    pass

class Son_1(Son):
    # Father.__init__(Grandfather)
    # Son.__init__(Father)
    def work(self):
        super().work()
    pass

son_2= Son_1()

# son_2.sleep()
# son_2.work()
# Grandfather.work(son_2)
# son_2.excercise()
print(son_2.nose_size)
son_2.work()

