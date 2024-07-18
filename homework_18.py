class Car:
    def __init__(self, year=2020, manufacturer='', model='', mileage=0, fuel_consumption=0.0):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}, пробіг: {self.mileage} км, витрата палива: {self.fuel_consumption} л/100км"

car1 = Car(2021, 'Toyota', 'Corolla', 15000, 6.5)
car2 = Car(2019, 'Honda', 'Civic', 25000, 5.8)
car3 = Car(manufacturer='Tesla', model='Model S', fuel_consumption=0.0)


print(car1)
print(car2)
print(car3)
