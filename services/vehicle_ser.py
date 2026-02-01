#SERVICES -- VEHICLE SER

from blueprint.vehicle import Vehicle

cars = []  #lIST WILL WORK AS A SIMPLE DATABASE

#DEFINED FUNCTION WHICH ADDS A NEW VEHICLE - VEHICLE_ID IS UNIQUE IN THIS CASE
def add_vehicle(vehicle_id: str, make: str, model: str, year: int, mileage: int, min_rent: int, max_rent: int):
    

    for c in cars:
        if c.vehicle_id == vehicle_id:
            print("Car ID already exists!")
            return None

    new_vehicle = Vehicle(vehicle_id, make, model, year, mileage, True, min_rent, max_rent)
    cars.append(new_vehicle)
    print(f"Car added: {vehicle_id} - {make} {model}")
    return new_vehicle

#DEFINED FUNCTION TO FIND THE CAR BY ITS ID
def find_vehicle_by_id(vehicle_id: str):
   
    for c in cars:
        if c.vehicle_id == vehicle_id:
            return c
    return None

#DEFINED FUNCTION TO UPDATE VEHICLE
def update_Vehicle(vehicle_id: str, field_name: str, new_value):

    vehicle = find_vehicle_by_id(vehicle_id)
    if not vehicle:
        print("Vehicle is not found!")
        return False

    # hasattr checks if that field exists in the object
    if not hasattr(vehicle, field_name):
        print("Invalid field name!")
        return False

    # setattr changes the attribute value
    setattr(vehicle, field_name, new_value)
    print(f"Updated car {vehicle_id}: {field_name} = {new_value}")
    return True

#DEFINED FUNCTION TO DELETE VEHICLE
def delete_vehicle(vehicle_id: str):

    vehicle = find_vehicle_by_id(vehicle_id)
    if not vehicle:
        print("Car not found!")
        return False

    cars.remove(vehicle)
    print(f"Vehicle deleted: {vehicle_id}")
    return True

#DEFINED FUNCTION TO DISPLAY ALL VEHICLES, WHERE AVAILABLE = TRUE
def list_vehicles(only_available: bool = False):
    
    if len(cars) == 0:
        print("No cars in the system yet.")
        return

    print("\n--- Vehicles ---")
    for c in cars:
        if only_available and not c.available:
            continue

        status = "Available ✅" if c.available else "Not Available ❌"
        print(
            f"ID: {c.vehicle_id} | {c.make} {c.model} | Year: {c.year} | "
            f"Mileage: {c.mileage} | {status} | MinDays: {c.min_rent} | MaxDays: {c.max_rent}"
        )
