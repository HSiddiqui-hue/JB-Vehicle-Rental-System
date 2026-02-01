#BLUEPRINT -- VEHICLE MODELS

#DEFINED CLASS VEHICLE (REPRESENTS ONE RECORD IN THE SYSTEM)
class Vehicle:

    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        year: int,
        mileage: int,
        available: bool = True,
        min_rent: int = 1,
        max_rent: int = 40
    ):

       # CREATES A VEHICLE OBJECT WITH THE VALUES, DEFAULTING AVAILABLE TO TRUE IF ITS NOT GIVEN
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available
        self.min_rent = min_rent
        self.max_rent = max_rent
