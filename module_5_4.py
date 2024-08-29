from random import choice, randint


class Buiding:
    total = 0
    def __init__(self, name='Объект'):
        """  Инициализация объекта класса  """
        self.name = name
        self.numberOfFloors = randint(1, 100)
        self.buildingType = choice(['кирпичное', 'панельное', 'каменное', 'бревенчатое', 'из соломы'])
        Buiding.total +=1

    def __str__(self):


        return str(self.__dict__)

     


buid_list = [Buiding('Объект №'+str(i)) for i in range(1, 41)]

print(*buid_list)
print('Всего объектов:', Buiding.total)