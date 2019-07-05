class MonederoSensor:
    def __init__(self):
        self.dinero = 1000

    def get_dinero(self):
        return self.dinero

    def quitar_dinero(self, dinero):
        self.dinero -= dinero

    def poner_dinero(self, dinero):
        self.dinero += dinero


class Machine_State:

    def __init__(self):
        self.water_level = 0
        self.coffe_level = 0
        self.pago = 0        
        self.sugar_level = 0
        self.coins = 0
        self.ready_to_coffe = False
        self.pay = False

    def add_water(self,count):
        self.water_level += count
    def remove_water(self,count):
        self.water_level -= count
    def state_water(self):
        return self.water_level
    def add_coffe(self,count):
        self.coffe_level += count
    def remove_coffe(self,count):
        self.coffe_level -= count
    def state_coffe(self):
        return self.coffe_level
    def add_sugar(self,count):
        self.sugar_level += count
    def remove_sugar(self,count):
        self.sugar_level -= count
    def state_sugar(self):
        return self.sugar_level

    def check_amount(self):
        if self.water_level < 100:
            return False
        if self.coffe_level < 10:
            return False
        if self.sugar_level < 5:
            return False
        else:
            return True

    def payment(self,coin):
        self.coins = coin
        pago = coin*10
        self.pay = True
        self.poner_dinero(pago)
        return

    def ret_payment(self):
        monedas = self.coins
        self.quitar_dinero(self.pago)
        self.coins = 0
        return monedas
        

class BaseCoffe(Machine_State,MonederoSensor):

    def __init__(self):
        super().__init__()
        self.ready_to_coffe = self.check_amount       

    def making_coffe(self,agua,azucar):
        if self.ready_to_coffe and self.pay:
            self.remove_coffe(10)
            self.remove_water(agua)
            if azucar == True:
                self.remove_sugar(5)
            return 'Su cafe esta listo.'
        else:
            if self.ready_to_coffe == False:
                monedas = self.ret_payment()
                return 'Esta maquina esta vacia tome sus '+ str(monedas) +'monedas'
            if self.pay == False:
                return 'No realizo ningun pago'

class PremiumCoffe(Machine_State,MonederoSensor):

    def __init__(self):
        super().__init__()

