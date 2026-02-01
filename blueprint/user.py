# BLUEPRINT -- USER MODELS
# IMPORTANT: usname = username


#DEFINED CLASS USER (STAFF + CLIENT)
class User: #BASE CLASS

    #DEFINED A FUNCTION WITH A CONSTRUCTOR ATRRIBUTE - WILL RUN AUTOMATICALLY WHEN OBJECT IS CREATED
    def __init__(self, usname: str, password: str):
       
        #SELF STORES THE DATA INSIDE THE OBJECT
        self.usname = usname
        self.password = password

#DEFINED CLASS USER (CLIENT)
class Client(User): #OBTAINED FROM USER CLASS
    
    #DEFINED A FUNCTION WITH A CONSTRUCTOR ATRRIBUTE - WILL RUN AUTOMATICALLY WHEN OBJECT IS CREATED
    def __init__(self, usname: str, password: str):
        #SUPER REFERS THE FUCTION TO GO THE BASE CLASS AND CALL OUT _INIT_
        super().__init__(usname, password)

        #THIS WILL ALLOW CLIENTS TO DO THEIR OWN RESERVATION
        self.reservation = []  # starts empty

#DEFINED CLASS USER (STAFF)
class Staff(User): #OBTAINED FROM USER CLASS
    #NOTE: ADMIN DOESN'T REQUIRES RESERVATION LIST AS THEY MANAGE VEHICLES RESERVATION.

    #DEFINED A FUNCTION WITH A CONSTRUCTOR ATRRIBUTE - WILL RUN AUTOMATICALLY WHEN OBJECT IS CREATED
    def __init__(self, usname: str, password: str):
        #SUPER REFERS THE FUCTION TO GO THE BASE CLASS AND CALL OUT _INIT_
        super().__init__(usname, password)
