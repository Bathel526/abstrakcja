from abc import ABC, abstractmethod

class KlasaAbstrakcyjna(ABC):
    def __init__(self):
        raise Exception('Nie mozna wywolywac klasy abstrakcyjnej')

    @abstractmethod   ## taki ala komentarz ze jest to metoda abstakcyjna
    def method_1(self):
        raise NotImplementedError('musisz zaimplementowac ta metode bo bedzie blad')

    @abstractmethod
    def method_2(self):
        pass # brak implementacji nie zglosi takiego leganckego komunikatu jak na gorze

class Test(KlasaAbstrakcyjna):
    def __init__(self, name):
        self.name = name

    #def method_1(self):
    #   print(self.name)

    def method_2(self):
        print('jem kanapke')

    def test_function(self):
        print('Just checking')


#test1 = MetodaAbstrakcyjna()

test2 = Test('Bart')
test2.method_1()