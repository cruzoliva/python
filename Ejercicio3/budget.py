
from tokenize import Name
from unicodedata import name


class Category:
    name = ""
    ledger = []
    def __init__(self, Name) -> None:
        self.name = Name
    
    def deposit(self, dep_amount, dep_description = ""):
        item = LedgerItem(dep_amount, dep_description)
        self.ledger.append(item)

    def check_funds(self, Amount) -> bool:
        acum = 0
        for LedgItem in self.ledger:
            acum = acum + LedgItem.amount
        
        return acum > Amount

    def withdraw(self, amount, description) -> bool:
        if self.check_funds(amount):
            item = LedgerItem(amount * -1, description)
            self.ledger.append(item)
            return True
        else:
            return False

    def transfer(self, amount, category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Trasfer to {category.name}")
            category.deposit(amount, f"Transfered from {self.name}")
            return True
        else:
            return False

    def get_balance(self):
        acum = 0
        asteriscos1 = (30 - len(self.name)) // 2 
        asteriscos2 = 30 - asteriscos1 - len(self.name)
        asteriscosiz = "".rjust(asteriscos1, "*")
        asteriscosde = "".rjust(asteriscos2, "*")
        print(f"{asteriscosiz}{self.name}{asteriscosde}")
        #Le doy formato al print para que los valores se visualicen como en el ejemplo 
        for LedgItem in self.ledger:
            print("{:<23}{:>7}".format(LedgItem.description, LedgItem.amount))
            #print("{:23}".format(LedgItem.description), "{:>7.2f}".format(LedgItem.amount))
            acum = acum + LedgItem.amount

        print("Total: " + "{:>7.2f}".format(acum))

        #Verifico el largo del nombre de la categoría para poder agregar los asteriscos 
        lenName = len(self.name)
        print(lenName)

class LedgerItem:
    amount = 0
    description = ""

    def __init__(self, Amount, Description) -> None:
        self.amount = Amount
        self.description = Description


#def create_spend_chart(categories, chart):









#cars = Category("Autos")
#cars.deposit(10000, "Inicial")
#pude = cars.withdraw(300, "nafta")
#pude = cars.withdraw(900, "Seguro")
#pude = cars.withdraw(100, "nafta")

#clothes = Category("Ropa")
#clothes.get_balance()

#cars.transfer(30, clothes)
#if pude == False:
#    print("No hay saldo")
#cars.get_balance()

