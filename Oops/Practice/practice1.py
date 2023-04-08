class Programmer:
    compani = "Microsoft"

    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The Name of the Programer is {self.name} and the product is {self.product}")

Harry = Programmer("harry","Skype")
Alka = Programmer("alka","Github")
Harry.getInfo()
Alka.getInfo()
