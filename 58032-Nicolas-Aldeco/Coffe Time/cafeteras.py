
class Machine():

    def __init__(self):
        self.water_level = 1000
        self.coffe_level = 100
        self.sugar_level = 100
        self.coins = 0

class BasicCoffeMaker(Machine):
    def __init__(self):
        super().__init__()
        self.makingCoffe = False

    def pago(self,coin):
        if coin == True:
            self.coins += 1
            self.makingCoffe = True
            return '-Haciendo Cafe-'
        else:
            return
    
    def coffequantity(self,coffe):
        if self.coffe_level > 0:
            self.coffe_level -= coffe
            return 'Cafe con '+str(coffe)+' gramos.'
        else:
            return 'No tengo mas cafe'

    def waterquantity(self,water):
        if self.water_level > 0:
            self.water_level -= water
            return 'Cafe con '+str(water)+' ml de agua'
        else:
            return 'No tengo mas agua'

    def sugarquantity(self,sugar):
        if self.sugar_level > 0 and sugar == True:
            self.sugar_level -= 5
            return 'Con azucar'
        elif sugar == False:
            return 'Sin azucar'
        else:
            return 'No tengo mas azucar'