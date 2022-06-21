from budget import *


cars = Category("Autos")
clothes = Category("Ropa")

cars.deposit(10000, "Inicial")
pude = cars.withdraw(300, "nafta")
pude = cars.withdraw(9000, "Seguro")
pude = cars.withdraw(1000, "nafta")
cars.transfer(30, clothes)
if pude == False:
    print("No hay saldo")
cars.get_balance()
clothes.get_balance()