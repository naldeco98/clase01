
class MonederoSensor:
    def __init__(self):
        self.dinero = 1000

    def get_dinero(self):
        return self.dinero

    def quitar_dinero(self, dinero):
        self.dinero -= dinero

    def poner_dinero(self, dinero):
        self.dinero += dinero

class MachineForCoffe(MonederoSensor):

    def __init__(self):
        super().__init__()
        self.water_level = 1000
        self.coffe_level = 100
        self.sugar_level = 100
        self.makingCoffe = False 
        self.money = 0

    def pago(self,coin):
        self.money = coin*10
        self.poner_dinero(money)
        if money == True:
            if self.coffe_level == 0:
                self.quitar_dinero(self.money)
                return 'Disculpe no tengo mas cafe. Tome su/sus monedas'
            if self.water_level == 0:
                self.quitar_dinero(self.money)
                return 'Disculpe no tengo mas cafe. Tome su/sus monedas'
            self.makingCoffe = True
            return '-Haciendo Cafe-'
        else:
            return 'Ingrese monedas por favor'

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
            self.water_level -= water
            return 'Cafe con '+str(water)+' ml de agua'

    def sugarquantity(self,sugar):
        if self.makingCoffe == True:
            if self.sugar_level > 0 and sugar == True:
                self.sugar_level -= 5
                return 'Con azucar'
            elif sugar == False:
                return 'Sin azucar'
            else:
                self.makingCoffe = False  
                self.quitar_dinero(self.money)       
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
                if self.money > 10:
                    self.coffetipe = 'Cafe con leche'
                    self.milklevel -= 100
                    return 'Cafe con leche'
                else:
                    self.quitar_dinero(self.money)
                    self.makingCoffe = False
                    return 'No alcanza el dinero, debe ingresar mas dinero.'
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
            self.water_level -= water
            return self.coffetipe +' con '+str(water)+' ml de agua'

    def sugarquantity(self,sugar):
        if self.makingCoffe == True:
            self.sugar_level -= sugar
            return self.coffetipe +' con '+str(sugar)+' gramos.'