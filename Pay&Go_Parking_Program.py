#parking lots system
#Group 7 - Kyle , Junxian, Mavros
#finished time: 2023/11/22

#make datetime is today
import datetime    
x = datetime.datetime.now()
year=x.year
month=x.month
day=x.day

#menu for user to choose
def print_menu():
    print("************************************************************")
    print("***Welcome to Park and GO Parking Application!***")
    print("Park from 6 PM - Midnight for a flat fee of $4.00")
    print("************************************************************")
    print("Select from the following options")
    print("1- Register a vehicle")
    print("2- Verify vehicle registration")
    print("3- Display registered vehicles")
    print("4- Display daily charges")
    print("5- Remove a vehicle")
    print("6- Clear vehicles")
    print("0- Exit")
    user_menu_input = input(">>> ")
    return int(user_menu_input)

#press enter to continue
def prompt():
    input("Please press enter to continue...")

#1-Register a vehicle
def register_vehicle(register_list, credit_card_list):
    user_plate_number = input("Enter your plate number: ")
    if user_plate_number in register_list:
        print(f"{user_plate_number} is already registered.")
    else:
        user_credit_card = input("Enter your Credit Card Number ($4.00 charge): ")
        register_list.append(user_plate_number)
        credit_card_list.append(user_credit_card)
        print(f"Thank you, your plate {user_plate_number} has been added to the lot.")
    prompt()    

#check password is right or not
def check_password():
    user_password=input("Enter your password: ")
    while user_password!="password":
            print("Password is incorrect!")
            prompt()
            print_menu()
            user_password=input("Enter your password: ")
          
    
#2-Verify vehicle registration
def verify_vehicle(user_plate_number, register_list):
    if user_plate_number in register_list:
        print(f"The vehicle with plate# {user_plate_number} is registered in the lot.")
    else:
        print("The vehicle is NOT registered.")
    prompt()      



#3-Display registered vehicles and save them to a file
def display_vehicles(register_list):
    if len(register_list) > 0:
        print(f"A list of registered vehicles for {year}-{month}-{day}")
        print("=======================")
        print(f"{'Plate':>12}")
        print("=======================")
        for plate in register_list:
            print(f"{plate:>10}")
        print("=======================")
        #create vehicles.txt file to record
        my_file=open('vehicles.txt','w')
        my_file.write(f"A list of registered vehicles for {year}-{month}-{day}\n")
        my_file.write("=======================\n")
        my_file.write(f"{'Plate':>12}\n")
        my_file.write("=======================\n")
        for plate in register_list:
            my_file.write(f"{plate:>10}\n")
        my_file.write("=======================\n")
        my_file.close()
    else:
        print("The parking lot is empty!")
    prompt()    

#4-Display daily charges and save them to a file
def display_charges(register_list):
    print(f"Daily parking summary for {year}-{month}-{day}")
    print("===================================================")
    print(f"{'Plate':12}{'Credit Card':<20}{'Charge in $':<20}")
    total_charge = 0
    for i in range(len(register_list)):
        plate = register_list[i]
        credit_card = credit_card_list[i]
        print(f"{plate:12}{credit_card:<20}4.00")
        total_charge += 4
    print("===================================================")
    print(f"{'Total':12}{total_charge:24.2f}")
    prompt()  

    #write into charges.txt
    my_file= open('charges.txt', 'w')
    my_file.write(f"Daily parking summary for {year}-{month}-{day}\n")
    my_file.write("===================================================\n")
    my_file.write(f"{'Plate':<12}{'Credit Card':<20}{'Charge in $':<20}\n")
    total_charge = 0
    for i in range(len(register_list)):
        plate = register_list[i]
        credit_card = credit_card_list[i]
        my_file.write(f"{plate:<12}{credit_card:<20}4.00\n")
        total_charge += 4 
    my_file.write("===================================================\n")
    my_file.write(f"{'Total':12}{total_charge:24.2f}\n")
    my_file.close()

#5-Remove a vehicle
def remove_vehicle(user_plate_number, register_list):
    if user_plate_number in register_list:
        register_list.remove(user_plate_number)
        print(f"{user_plate_number} is removed.")

        #remove in vehicles.txt
        my_file=open('vehicles.txt','w')
        for user_plate_number in register_list:
          my_file.write(f"A list of registered vehicles for {year}-{month}-{day}\n")
          my_file.write("=======================\n")
          my_file.write(f"{'Plate':>12}\n")
          my_file.write("=======================\n")
        for plate in register_list:
            my_file.write(f"{plate:>10}\n")
        my_file.write("=======================\n")
        my_file.close()

        #remove in charges.txt
        my_file= open('charges.txt', 'w')
        my_file.write(f"Daily parking summary for {year}-{month}-{day}\n")
        my_file.write("===================================================\n")
        my_file.write(f"{'Plate':<12}{'Credit Card':<20}{'Charge in $':<20}\n")
        total_charge = 0
        for i in range(len(register_list)):
            plate = register_list[i]
            credit_card = credit_card_list[i]
            my_file.write(f"{plate:<12}{credit_card:<20}4.00\n")
            total_charge += 4 
        my_file.write("===================================================\n")
        my_file.write(f"{'Total':12}{total_charge:24.2f}\n")
        my_file.close()

    else:
        print(f"{user_plate_number} is not registered.")
    prompt()      

#6-Clear vehicles
def clear_vehicles(register_list):
    register_list.clear()
    print("All vehicles were removed, and the lot is empty.")
    prompt()  

    #clear charges.txt
    my_file= open('charges.txt', 'w')
    my_file.close()
    #clear vehicle.txt
    my_file=open('vehicles.txt','w')
    my_file.close()

# Application start
register_list = []
credit_card_list = []
spaceforcar=4   #parking lot has only 4 spots

while True:
    user_menu_input = print_menu()          #run menu until user choose 0 to exit

    if user_menu_input == 1:
        if len(register_list)<spaceforcar:
            print("The parking lot has spaces for your vehicle.")
            register_vehicle(register_list, credit_card_list)
        else:
            print("The paking lot is full now.")
    elif user_menu_input == 2:
        print("Verify your registration")
        user_password_input=check_password()
        user_plate_number = input("Enter plate number: ")
        verify_vehicle(user_plate_number, register_list)
    elif user_menu_input == 3:
        user_password_input=check_password()
        display_vehicles(register_list)
        
    elif user_menu_input == 4:
        user_password_input=check_password()
        display_charges(register_list)
        
    elif user_menu_input == 5:
        user_password_input=check_password()
        user_plate_number = input("Enter the plate number to remove: ")
        remove_vehicle(user_plate_number, register_list)

    elif user_menu_input == 6:
        user_password_input=check_password()
        clear_vehicles(register_list)
        
    elif user_menu_input == 0:
        print("Thanks and Good Bye!")
        break
    else:
        print("Invalid Input")
        prompt()
