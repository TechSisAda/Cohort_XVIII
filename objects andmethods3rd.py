class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def __str__(self) -> str:
        return f"{self.brand} {self.color}"
    
my_car = Car("Toyota", "Grey")
print(my_car)