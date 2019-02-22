#Animals and Object Oriented Programming

class Animal():

    def __init__(self, name, _class, diet, schedule):
        self.name = name
        self._class = _class
        self.diet = diet
        self.schedule = schedule
        return

        #We've made this such that no matter the amount of args, we will always print them all
    def __str__(self):
        str=""
        i = 0
        #print(self.__dict__.items()) debugging purposes
        for atr, val in self.__dict__.items():
            str+='['+atr+']'+ ":"+ val+'\n' #shouldn't use += cause it takes O(n) but for now its good enough
            if i > 0:
                str+='\t'
            i+=1
        return str

    def eats(self):
        return self.diet

    def schedule(self):
        return self.schedule


class Mammal(Animal):

    def __init__(self, name,diet,schedule):
        super().__init__(name=name, _class="Mammal",diet=diet,schedule=schedule)
        return


class Reptile(Animal):

    def __init__(self, name,diet,schedule):
        super().__init__(name=name, _class="Reptile",diet=diet,schedule=schedule)
        return


class Amphibian(Animal):

    def __init__(self, name,diet,schedule):
        super().__init__( name=name, _class="Amphibian",diet=diet,schedule=schedule)
        return
