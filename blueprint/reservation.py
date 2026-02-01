#BLUEPRINT -- RESERVATION MODELS

#IMPORTED DATE AND TIME CLASS TO MANAGE THE SCHEDULE OF VEHICLE RENTALS
from datetime import datetime

##DEFINED RESERVATION - REPRESENTS A RENTAL REQUEST - FLOW: PENDING: APPROVED & PENDING: REJECTED
class Reservation:
   
    #DEFINED A FUNCTION WITH A CONSTRUCTOR ATRRIBUTE - WILL RUN AUTOMATICALLY WHEN OBJECT IS CREATED
    def __init__(self, reservation_id: str, client, vehicle, start_date: str, end_date: str):
      
        self.reservation_id = reservation_id
        self.client = client
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Pending"  # THIS IS SET TO DEFAULT

    #DEFINED A FUNCTION WHICH CALCULATES RENTAL DURATION
    def hire_days(self) -> int:
       #PARSE STRING DATES INTO DATETIME USING STRPTIME
        fmt = "%Y-%m-%d"
        start = datetime.strptime(self.start_date, fmt)
        end = datetime.strptime(self.end_date, fmt)

        #THIS LAST LINE WILL GIVE DIFFERENCE HOWEVER IF RENTED ON THE SAME DAY IT TURNS INTO 0
        # THEN WE ADDED +1 TO COUNT AN ADDITIONAL DAYS
        return (end - start).days + 1

    #DEFINED A FUNCTION WHICH CALCULATES CHARGES
    def calculate_charges(self) -> int:
        Base_rate_per_day = 50
        return Base_rate_per_day * self.hire_days()
