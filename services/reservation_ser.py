#SERVICES -- RESERVATION SER

#IMPORTING KEY CLASSES AND ATTRIBUTES

from blueprint.reservation import Reservation
from services.vehicle_ser import find_vehicle_by_id

reservations = []  #LIST OF RESEVATION OBJECTS

#DEFINED A FUNCTION WHICH HANDLES CLIENT RESERV REQ BY VALIDATING BELOW MENTIONED PARAMETERS
def create_reservation(reservation_id: str, client, vehicle_id: str, start_date: str, end_date: str):

    vehicle = find_vehicle_by_id(vehicle_id)
    if not vehicle:
        print("Car not found!")
        return None

    if not vehicle.available:
        print("Car is not available right now!")
        return None

    new_reservation = Reservation(reservation_id, client, vehicle, start_date, end_date)

    # Check min/max rent constraints
    days = new_reservation.hire_days()
    if days < vehicle.min_rent or days > vehicle.max_rent:
        print(f"Rental period must be between {vehicle.min_rent} and {vehicle.max_rent} days.")
        return None

    reservations.append(new_reservation)
    client.reservation.append(new_reservation)

    print(f"Reservation created (Pending): {reservation_id}")
    print(f"Fee estimate: NZ${new_reservation.calculate_charges()}")
    return new_reservation


#DEFINED A FUNCTION WHICH FINDS RESERVATION BY ID
def find_reservation_by_id(reservation_id: str):
    for b in reservations:
        if b.reservation_id == reservation_id:
            return b
    return None

#DEFINED A FUNCTION WHICH APPROVES RESERVATION (STAFF)
def approve_reservation(reservation_id: str):

    b = find_reservation_by_id(reservation_id)
    if not b:
        print("Reservation not found!")
        return False

    if b.status != "Pending":
        print("Only Pending reservations can be approved/rejected.")
        return False

    b.status = "Approved"
    b.vehicle.available = False  # car is now rented
    print(f"Reservation approved: {reservation_id}")
    return True

#DEFINED A FUNCTION WHICH REJECTS RESERVATION (STAFF)
def reject_reservation(reservation_id: str):

    b = find_reservation_by_id(reservation_id)
    if not b:
        print("Reservation not found!")
        return False

    if b.status != "Pending":
        print("Only Pending reservation can be approved/rejected.")
        return False

    b.status = "Rejected"
    print(f"Reservation rejected: {reservation_id}")
    return True

#DEFINED A FUNCTION WHICH DISPLAY ALL RESERVATIONS
def list_all_reservation():
    
    if len(reservations) == 0:
        print("No reservation yet.")
        return

    print("\n--- Reservations ---")
    for b in reservations:
        print(
            f"ID: {b.reservation_id} | Client: {b.client.usname} | "
            f"Vehicle: {b.vehicle.vehicle_id} ({b.vehicle.make} {b.vehicle.model}) | "
            f"{b.start_date} -> {b.end_date} | Days: {b.hire_days()} | "
            f"Status: {b.status} | Fee: ${b.calculate_charges()}"
        )

#DEFINED AN INNOVATIVE FEATURE - staff DASHBOARD FOR QUICK DECISION MAKING
def staff_dashboard_summary():

    total = len(reservations)
    pending = len([b for b in reservations if b.status == "Pending"])
    approved = len([b for b in reservations if b.status == "Approved"])
    rejected = len([b for b in reservations if b.status == "Rejected"])

    print("\n--- Staff Dashboard Summary ---")
    print(f"Total reservation: {total}")
    print(f"Pending: {pending}")
    print(f"Approved: {approved}")
    print(f"Rejected: {rejected}")
