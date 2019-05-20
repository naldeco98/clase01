
class MachineForCoffe():

    def __init__(self):
        self.water_level = 1000
        self.coffe_level = 100
        self.sugar_level = 100
        self.coins = 0
        self.makingCoffe = False 

    def pago(self,coin):
        if coin == True:
            self.coins += 1
            if self.coffe_level == 0:
                self.coins -= 1
                return 'Disculpe no tengo mas cafe. Tome su moneda'
            self.makingCoffe = True
            return '-Haciendo Cafe-'
        else:
            return 'Ingrese una moneda por favor'

class BasicCoffeMaker(MachineForCoffe):
    def __init__(self):
        super().__init__()
    
    def coffequantity(self,coffe):
        if self.makingCoffe == True:
            self.coffe_level -= coffe
            return 'Cafe con '+str(coffe)+' gramos.'
        else:
            return

    def waterquantity(self,water):
        if self.makingCoffe == True:
            if self.water_level > 0:
                self.water_level -= water
                return 'Cafe con '+str(water)+' ml de agua'
            else:
                self.coins -= 1
                self.makingCoffe = False
                return 'No tengo mas agua,tome su moneda'
        else:
            return

    def sugarquantity(self,sugar):
        if self.makingCoffe == True:
            if self.sugar_level > 0 and sugar == True:
                self.sugar_level -= 5
                return 'Con azucar'
            elif sugar == False:
                return 'Sin azucar'
            else:
                self.coins -= 1
                self.makingCoffe = False         
                return 'No tengo mas azucar,tome su moneda'
        else:
            return

class PremiumCoffeMaker(MachineForCoffe):

    def __init__(self):

        super().__init__()
        self.cup = False
        self.coffetipe = ''
        self.milklevel = 1000

    def cupcheck(self,cup):
        if cup == False:
            self.makingCoffe = False
            return 'Ponga un vaso por favor'
        else:
            self.makingCoffe = True
            return 'Vaso en compartimiento'

    def withmilk(self,milk):
        if self.makingCoffe == True:
            if milk == True:
                self.coffetipe = 'Cafe con leche'
                self.milklevel -= 100
                return 'Cafe con leche'
            else:
                self.coffetipe = 'Cafe'
                return 'Cafe solo'
        else:
            return

    def coffequantity(self,coffe):
        if self.makingCoffe == True:
            if self.coffe_level > 0:
                self.coffe_level -= coffe
                return self.coffetipe +' con '+str(coffe)+' gramos.'
            else:
                self.coins -= 1
                self.makingCoffe = False
                return 'No tengo mas cafe,tome su moneda'
        else:
            return

    def waterquantity(self,water):
        if self.makingCoffe == True:
            if self.water_level > 0:
                self.water_level -= water
                return self.coffetipe +' con '+str(water)+' ml de agua'
            else:
                self.coins -= 1
                self.makingCoffe = False
                return 'No tengo mas agua,tome su moneda'
        else:
            return

    def sugarquantity(self,sugar):
        if self.makingCoffe == True:
            self.sugar_level -= sugar
            return self.coffetipe +' con '+str(sugar)+' gramos.'