# MAIN FILE 

from blueprint.user import Client, Staff
from services.user_ser import signup_user, login_user
from services.vehicle_ser import add_vehicle, update_Vehicle, delete_vehicle, list_vehicles
from services.reservation_ser import (
    create_reservation, approve_reservation, reject_reservation,
    list_all_reservation, staff_dashboard_summary
)

#DEFINED FUNCTION TO SHOW STAFF MENU WHICH ALLOW THEM TO MANAGE VEH - RESERVATIONS - VIEW DASHBOARD
def staff_menu():
   
    while True:
        print("\n========= STAFF MENU =========")
        print("1) Add Vehicle")
        print("2) Update Vehicle")
        print("3) Delete Vehicle")
        print("4) View All Vehicle")
        print("5) View Available Vehicle")
        print("6) View All Reservations")
        print("7) Approve Reservation")
        print("8) Reject Reservation")
        print("9) Dashboard Summary (Innovative)")
        print("0) Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            vehicle_id = input("Vehicle ID: ").strip()
            make = input("Make: ").strip()
            model = input("Model: ").strip()
            year = int(input("Year: ").strip())
            mileage = int(input("Mileage: ").strip())
            min_rent = int(input("Min rent days: ").strip())
            max_rent = int(input("Max rent days: ").strip())
            add_vehicle(vehicle_id, make, model, year, mileage, min_rent, max_rent)

        elif choice == "2":
            vehicle_id = input("Vehicle ID to update: ").strip()
            field = input("Field (make/model/year/mileage/available/min_rent/max_rent): ").strip()
            value = input("New value: ").strip()

            # Convert to correct type
            if field in ["year", "mileage", "min_rent", "max_rent"]:
                value = int(value)
            elif field == "available":
                value = True if value.lower() == "true" else False

            update_Vehicle(vehicle_id, field, value)

        elif choice == "3":
            car_id = input("Vehicle ID to delete: ").strip()
            delete_vehicle(car_id)

        elif choice == "4":
            list_vehicles(only_available=False)

        elif choice == "5":
            list_vehicles(only_available=True)

        elif choice == "6":
            list_all_reservation()

        elif choice == "7":
            booking_id = input("Booking ID to approve: ").strip()
            approve_reservation(booking_id)

        elif choice == "8":
            booking_id = input("Booking ID to reject: ").strip()
            reject_reservation(booking_id)

        elif choice == "9":
            staff_dashboard_summary()

        elif choice == "0":
            print("Logging out...")
            break

        else:
            print("❌ Invalid choice.")

#PROVIDES A CUSTOMER MENU TO VIEW AVAILABLE CARS, MAKE BOOKINGS, SEE THEIR BOOKINGS, AND 
#RECEIVE SIMPLE AVAILABILITY ALERTS.
def client_menu(Client: Client):
    
    while True:
        print("\n========= CLIENT MENU =========")
        print("1) View Available Vehicles")
        print("2) Book a Vehicle")
        print("3) View My Reservation")
        print("0) Logout")

        choice = input("Choose: ").strip()

        if choice == "1":
            list_vehicles(only_available=True)

        elif choice == "2":
            # "Availability alert" (small innovation): show cars first so user doesn't guess
            print("\nTip: Here are available cars right now:")
            list_vehicles(only_available=True)

            reservation_id = input("Reservation ID (example B001): ").strip()
            vehicle_id = input("Car ID to book: ").strip()
            start_date = input("Start date (YYYY-MM-DD): ").strip()
            end_date = input("End date (YYYY-MM-DD): ").strip()

            create_reservation(reservation_id, Client, vehicle_id, start_date, end_date)

        elif choice == "3":
            if len(Client.reservation) == 0:
                print("You have no bookings yet.")
            else:
                print("\n--- My Reservation ---")
                for b in Client.reservation:
                    print(
                        f"ID: {b.reservation_id} | Vehicle: {b.vehicle.make} {b.vehicle.model} | "
                        f"{b.start_date}->{b.end_date} | Status: {b.status} | Fee: ${b.calculate_charges()}"
                    )

        elif choice == "0":
            print("Logging out...")
            break

        else:
            print("Invalid choice.")


#DEFINED MAIN PROGRAM CLI VERSION FOR STAFF AND CLIENT TO USE
def main():
   
    print("===================================")
    print("      WELCOME TO JB CAR RENTALS     ")
    print("===================================")

    while True:
        print("\n========= MAIN MENU =========")
        print("1) Sign Up")
        print("2) Login")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            usname = input("Username: ").strip()
            password = input("Password: ").strip()
            role = input("Role (staff/client): ").strip()
            signup_user(usname, password, role)

        elif choice == "2":
            usname = input("Username: ").strip()
            password = input("Password: ").strip()
            user = login_user(usname, password)

            if user:
                # Role-based menu
                if isinstance(user, Staff):
                    staff_menu()
                else:
                    client_menu(user)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
