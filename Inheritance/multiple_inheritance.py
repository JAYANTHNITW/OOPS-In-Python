class Male:
    def __init__(self,num_heart=2):
        print('calling init from male')
        self.num_eyes=2
        self.num_nose=1
        self.num_heart= num_heart
    def work(self):
        print('I will code daily')

    def sleep(self):
        print('i will sleep 6hours daily')

class Female:
    def __init__(self,name):
        self.name=name
    def work(self):
        print('Daily i will wash clothes')

    def clean(self):
        print('Daily i will clean the house')


class Boy(Male,Female):
    def __init__(self,name,language):
        self.language = language
        Female.__init__(self,name)
        Male.__init__(self,num_heart=3)

    def display(self):
        return f"Hi iam {self.name} and i work on {self.language}"



boy_1 = Boy('jay','python')
#print(Female.__init__(boy_1))
print(boy_1.num_nose)
print(boy_1.num_heart)
print(boy_1.language)
print(boy_1.display())
