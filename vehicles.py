# class vehicles:
#     def __init__(self,model,brand,color):
#         self.vehiclemodel=model
#         self.vehiclebrand=brand
#         self.vehiclecolor=color
#
#     def display(self):
#         print(self.vehiclemodel,self.vehiclebrand,self.vehiclecolor)
#
#
# vehicle1=vehicles("pick up","Mitsubishi","Grey")
# vehicle1.display()
# vehicle2=vehicles("lorry","Toyota","White")
# vehicle2.display()
# vehicle3=vehicles("Car","BMW","Black")
# vehicle3.display()


class vehicle:
    def __init__(self, model, brand, color):
        self.vehiclemodel = model
        self.vehiclebrand = brand
        self.vehiclecolor = color

    def display(self):
        print(self.vehiclemodel, self.vehiclebrand, self.vehiclecolor)


class Mitsubishi(vehicle):
    pass


mitsubishi = Mitsubishi("Mistubishi", "Pick up", "Grey")
mitsubishi.display()


class Toyota(vehicle):
    pass


toyota = Toyota("Toyota", "Lorry", "White")
toyota.display()


class BMW(vehicle):
    pass


bMW = BMW("BMW", "Car", "Black")
bMW.display()
