# Make a car rental system in OOPs
# 1. You have to register the cars asking car model, year of purchase, car number
# 2. Once car is registered you have make a display method to display cars that are availabe
# 3. Now you have to create another class to rent the car

# some important points
# Store the cars in a storage
# If someone rents the car ask for how much time you want to rent the car
# If the car is rented out remove that car from the storage as well.

class Car_info:
    def __init__(self, car_name, model, year, car_num):
        self.car_name = car_name
        self.model = model
        self.year = year
        self.car_num = car_num
        self.is_avai = True
        
    def display(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Car Number: {self.car_num}")
        print(f"Is Available: {self.is_avai}")
        
class CarRental:
    def __init__(self):
        self.cars = []
        
    def register_car(self, car_name, model, year, car_num):
        car = Car_info(car_name, model, year, car_num)
        self.cars.append(car)
        
    def diaplay_cars(self):
        available_cars = [car for car in self.cars if car.is_avai]
        if available_cars:
            for car in available_cars:
                car.display()
        else:
            print("No cars available")
        
        
    def rent_car(self, car_num, rent_dura):
        for car in self.cars:
            if car.car_num == car_num:
                car.is_avai = False  
                print(f"car {car_num} is rented for {rent_dura} days")
                break
        else:
            print(f"Car {car_num} is not available for rent")  
        
        
car_rental = CarRental()

car_rental.register_car("Eon", "Hyundai-Eon", 2012, "MP 04 BR 1234")
car_rental.register_car("Eon", "MG-Hector", 2012, "MP 04 BR 1234")
car_rental.register_car("Eon", "Hyundai-Creata", 2012, "MP 04 BR 1234")
car_rental.register_car("Eon", "Hyundai-Verna", 2012, "MP 04 BR 1234")

car_rental.diaplay_cars()

car_rental.rent_car("MP 04 BR 1234", 5)

car_rental.diaplay_cars()