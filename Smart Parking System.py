class car:
    def __init__(self, plate_number, car_model, entry_time):
        self.plate_number = plate_number
        self.car_model = car_model
        self.entry_time = entry_time
    def display_info(self):
        return f"Car number: {self.plate_number} | Model: {self.car_model} | Entry time: {self.entry_time}"
# ParkingLot
class ParkinkLot:
    def __init__(self):
        self.cars_list = []
    def park_car(self, car_object):
        self.cars_list.append(car_object)
        print(f"Car number {car_object.plate_number} was successfully parked in the garage.")
    def show_all_cars(self):
        if len(self.cars_list) == 0:
            print("The garage is currently empty.")
        else:
            print("----List of cars in the garage----")
            for car in self.cars_list:
                print(car.display_info())
    def exit_car(self, plate_number):
        for car in self.cars_list:
            if car.plate_number == plate_number:
                self.cars_list.remove(car)
                print(f"Car number {plate_number} has left. Please visit up again!")
                return True
        print(f"Sorry, car number {plate_number} is not in the garage!")
        return False


garage = ParkinkLot()
while True:
    print("/n---Smart Garage Management System---")
    print("1.Park Car")
    print("2.Exit Car")
    print("3.Show All Cars")
    print("4.Exit")

    choice = input("Choose the number (1-4): ")
    if choice == "1":
        plate = input("Enter the car's license plate number: ")
        model = input("Enter the car model: ")
        time_in = input("Enter login time: ")

        new_car = car(plate, model, time_in)
        garage.park_car(new_car)
    elif choice == "2":
        plate = input("Enter the license plate number of the vehicle you wish to extract: ")
        garage.exit_car(plate)
    elif choice == "3":
        garage.show_all_cars()
    elif choice == "4":
        print("Thank you for using the garage system. Goodbye")
        break
    else:
        print("Please choose from number 1 to 4.")
                      
          
        
                              
        
        