class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.seats = seats
        self.fare = fare
    
    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seat aviable in the train are {self.seats}")

    def getfareInfo(self):
        print(f"The prise of the ticket is: {self.fare}")

intercity = Train("Intercity Express : 14015 " , 90 , 300)
intercity.getstatus()
intercity.getfareInfo()
