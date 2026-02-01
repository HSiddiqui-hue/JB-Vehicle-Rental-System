#SERVICES -- USER SER

from blueprint.user import Client, Staff

#DEFINED BUSINESS LOGIC, USING IN MEMORY DATA

users = []  #lIST WILL WORK AS A SIMPLE DATABASE

#DEFINED FUNCTION WHICH REGISTERS A USNAME WITH ROLE - CHECKS IF USER EXIST - CREATE OBJECT - STORED INFO
def signup_user(usname: str, password: str, role: str):

    #WILL HELP TO CHECK FOR ANY DUPLICATES 
    for u in users:
        if u.usname == usname:
            print("Username already taken!")
            return None

    role = role.lower().strip()

    if role == "staff":
        new_user = Staff(usname, password)
    else:
        # anything else becomes customer for beginner simplicity
        new_user = Client(usname, password)

    users.append(new_user)
    print(f"Registered {role} user: {usname}")
    return new_user

#DEFINED FUNCTION WHICH LOOPS THRU ALL USERS AND U+PW MATCH - IF MATCH RETURN THE U-OBJECT
def login_user(usname: str, password: str):

    for u in users:
        if u.usname == usname and u.password == password:
            print(f"Login successful. Welcome, {usname}!")
            return u

    print("Invalid username or password.")
    return None
