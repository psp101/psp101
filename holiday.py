

# This is a holiday cost calculating programme:
# There are many variables which could be included:
# in this first attempt, will make flights cost are return: there could be variable in day:
# hotel variables
# car rental variable
def Barcelona(): #city wise cost break down
    flight_cost = 45  # cost of light
    hotel_costper_night = 75  # cost per night in hotel
    car_rental_perday = 20  # cost of car rental by day
    return (flight_cost + (hotel_costper_night * nights) + (car_rental_days * car_rental_perday)) #total cost
def Lisbon():
    flight_cost = 40
    hotel_costper_night = 55
    car_rental_perday = 10
    return (flight_cost + (hotel_costper_night*nights)+(car_rental_perday*car_rental_days))
def Milan():
    flight_cost = 55
    hotel_costper_night = 80
    car_rental_perday_= 30
    return(flight_cost + (hotel_costper_night*nights)+(car_rental_perday_*car_rental_days))
def NewYork():
    flight_cost = 150
    hotel_costper_night = 85
    car_rental_perday = 50
    return (flight_cost + (hotel_costper_night * nights) + (car_rental_perday * car_rental_days))
def Budapest():
    flight_cost = 20
    hotel_costper_night = 55
    car_rental_perday = 55
    return(flight_cost + (hotel_costper_night*nights)+(car_rental_perday*car_rental_days))


def cities():  # option for user to select city
    print("cities:")
    print("1  Barcelona")
    print("2  Lisbon")
    print("3  Milan")
    print("4  New York")
    print("5 Budapest")
    print("6 quit the programme")

print(" This will calculated total holiday cost.")

while True:  # checking if the user entry
    cities()
    select_city = int(input("Select a city by number : "))

    if select_city == 6:
        break
    if select_city > 6:
        print("Wrong entry, Pleas select city 1-5, 6 to exit")
        break
    nights = int(input("Enter the number of nights:"))  # duration of the stay in hotel
    car_rental_days = int(input("Number of days for rental"))  # No. of days car is needed

    if select_city == 1:  # calculation using def funtion and user inpts
        print("Holiday cost for in barcelona", Barcelona())
    elif select_city == 2:
        print("Holiday cost for in lisbon", holiday())
    elif select_city == 3:
        print("Holiday cost for in Milan", holiday())
    elif select_city == 4:
        print("Holiday cost for in New York", holiday())
    elif select_city == 5:
        print("Holiday cost for in Budapest", holiday())
    else:
        print("Invalid selection, select form 1 -6")





