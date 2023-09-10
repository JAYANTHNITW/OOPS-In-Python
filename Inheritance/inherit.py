#print('Jayanth is the winner')

class Male:
    def work(self):
        print('I will code daily')

    def sleep(self):
        print('i will sleep 6hours daily')

class Female:
    def work(self):
        print('Daily i will wash clothes')

    def clean(self):
        print('Daily i will clean the house')


class Boy(Male,Female):
    pass

boy_1 = Boy()

boy_1.work()
print(boy_1.clean())