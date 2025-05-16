class Car:
    def __init__(self, car_id, brand, model_year,price, mileage):
        self.car_id = car_id
        self.brand = brand
        self.model_yar = model_year
        self.mileage = mileage
        self.price = price
    def __str__(self):
        return f"ID: {self.car_id}, Brand: {self.brand}, Year:{self.model_yar}, Price: ${self.price}, Mileage:{self.mileage}km"
car_listings = [
    Car(1, "Toyota", 2020, 20000, 25000),
    Car(2, "Honda", 2019, 18000, 30000),
    Car(3, "Ford", 2021, 22000, 20000),
    Car(4, "BMW", 2018, 28000, 40000),
    Car(5, "Hyundai", 2022, 19000, 15000)
]
def display_all_cars():
    if not car_listings:
        print("\nNo cars available.\n")
        return
    print("\n=== Car Listings ===")
    for i, car in enumerate(car_listings):
        print(f"{i}. {car}")
    print()



def add_car():
    try:
        car_id = int(input("Enter Car ID: "))
        brand = input("Enter Brand: ")
        model_year = int(input("Enter Model Year: "))
        price = float(input("Enter Price: "))
        mileage = int(input("Enter Mileage: "))
        car_listings.append(Car(car_id, brand, model_year, price, mileage))
        print("✅ Car added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Please try again.\n")


# --- Delete Car ---
def delete_car():
    try:
        index = int(input("Enter index of car to delete: "))
        if 0 <= index < len(car_listings):
            removed = car_listings.pop(index)
            print(f"✅ Removed: {removed}")
        else:
            print("❌ Invalid index.\n")
    except ValueError:
        print("❌ Invalid input.\n")


# --- Update Car ---
def update_car():
    try:
        index = int(input("Enter index of car to update: "))
        if 0 <= index < len(car_listings):
            car = car_listings[index]
            print(f"Editing: {car}")
            car.car_id = int(input("New Car ID: "))
            car.brand = input("New Brand: ")
            car.model_year = int(input("New Model Year: "))
            car.price = float(input("New Price: "))
            car.mileage = int(input("New Mileage: "))
            print("✅ Car updated.\n")
        else:
            print("❌ Invalid index.\n")
    except ValueError:
        print("❌ Invalid input.\n")


# --- Sort Cars ---
def sort_cars():
    print("\nSort By:")
    print("1. Price (Low to High)")
    print("2. Price (High to Low)")
    print("3. Model Year (Newest First)")
    print("4. Model Year (Oldest First)")
    choice = input("Enter your choice: ")

    if choice == '1':
        car_listings.sort(key=lambda car: car.price)
    elif choice == '2':
        car_listings.sort(key=lambda car: car.price, reverse=True)
    elif choice == '3':
        car_listings.sort(key=lambda car: car.model_year, reverse=True)
    elif choice == '4':
        car_listings.sort(key=lambda car: car.model_year)
    else:
        print("❌ Invalid choice.\n")
        return

    print("✅ Cars sorted.\n")
    display_all_cars()


# --- Filter by Brand ---
def filter_by_brand():
    brand_input = input("Enter brand to filter by: ").strip().lower()
    filtered = [car for car in car_listings if car.brand.lower() == brand_input]

    if filtered:
        print("\nFiltered Results:")
        for car in filtered:
            print(car)
    else:
        print(f"❌ No cars found for brand '{brand_input}'.")
    print()

def menu():
    while True:
        print("===== Car Listings Menu =====")
        print("1. View All Cars")
        print("2. Add New Car")
        print("3. Delete Car")
        print("4. Update Car")
        print("5. Sort Cars")
        print("6. Filter by Brand")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_cars()
        elif choice == '2':
            add_car()
        elif choice == '3':
            delete_car()
        elif choice == '4':
            update_car()
        elif choice == '5':
            sort_cars()
        elif choice == '6':
            filter_by_brand()
        elif choice == '0':
            print("🚗 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()