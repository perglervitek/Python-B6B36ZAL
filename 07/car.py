class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    # def setBrand(self,brand,price):
    #     self.brand = brand
    #     self.price = price

    def __str__(self):
        return "Car brand:" + self.brand + ", price " + str(self.price)

    def print(self):
        print("Car brand:", self.brand, str(self.price))
