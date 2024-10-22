import random
from datetime import datetime
class Train:
    def __init__(self, train_no,train_name,date,departure_time, arrival_time,fare):
        self.train_no = train_no
        self.train_name = train_name
        self.date = date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.fare = fare
        self.available_seats =50

    def display_train_details(self):
        print("\n=======Train Details=======")
        print(f"Train no:{self.train_no}")
        print(f"Train Name :{self.train_name}")
        print(f"Date:{self.date}")
        print(f"Departure_time:{self.departure_time}")
        print(f"Arrival_time:{self.arrival_time}")
        print(f"Fare:{self.fare}")
        print(f"Available_seats:{self.available_seats}")

class Ticket:
    def __init__(self,name,age,identity_no,gender,travel_class,berth,seat_no,pnr):
        self.name = name
        self.age = age
        self.identity_no = identity_no
        self.gender = gender
        self.travel_class = travel_class
        self.berth = berth
        self.seat_no = seat_no
        self.pnr = pnr
    def display_ticket(self):
        print(f"\n========Ticket Details=========")
        print(f"PNR:{self.pnr}")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Identity_no:{self.identity_no}")
        print(f"Gender:{self.gender}")
        print(f"Travel_class:{self.travel_class}")
        print(f"Berth:{self.berth}")
        print(f"Seat no:{self.seat_no}")
        print("booking status :successfull")

class TicketBookingSystem:
    def __init__(self):
        self.train = Train("12345","Rajadhani Express",self.get_today_date(),"10:00 AM","06:00 PM","Rs 500")
        self.users = {"user1":"password1", "user2":"password2"}
        
    
    def get_today_date(self):
        return datetime.now().strftime("%Y-%m-%d")
    def login(self):
        print("\n========Railway Ticket Booking Login=============")
        while True:
            username = input("enter username:")
            password = input("enter password:")
            if username in self.users and self.users[username]==password:
                print("\nLogin successfull!")
                return True
            else:
                print("Invalid username or password try again")
    def display_menu(self):
        print("\n=======Main Menu=========")
        print("1.Display Train Details")
        print("2.book ticket")
        print("3.exit")
    def book_ticket(self):
        if self.train.available_seats > 0:
            name = input("enter passenger name:")
            age = int(input("enter passenger age:"))
            identity_no = input("enter passenger idetity no:")
            gender = input("enter passenger gender (M\F):")      
            travel_class = input("enter class of travel(first/second/sleeper):")
            berth = self.choose_berth_preferences()
            print("berth selected:{berth}")
            # generate PNR NO
            pnr = f"PNR{random.randint(10000,99999)}"
            seat_no = 11-self.train.available_seats
            ticket = Ticket(name,age,identity_no,gender,travel_class,berth,seat_no,pnr)
            self.train.available_seats -= 1
            ticket.display_ticket()

            print(f" passenger {name}'s  ticket has been booked") 
        else:
            print("sorry no more seats available")      
    def choose_berth_preferences(self):
        print("\nchosse berth")
        print("1.Lower")
        print("2.Middle")
        print("3.upper") 
        berth_choice = input("enter your choice(1-3):")
        if berth_choice == '1':
            return 'lower'
        elif berth_choice == '2':
            return 'middle'  
        elif berth_choice == '3':
            return 'Upper'
        else:
            print("invalid choice")
    def start(self):
        if self.login():
            while True:
                self.display_menu()
                choice = input("enter your choice (1-3):")
                if choice == '1':
                    self.train.display_train_details()
                elif choice == '2':
                    self.book_ticket()
                elif choice == '3':
                    print("exiting the system.have a nice day.")
                    break
                else:
                    print("invalid choice try again")
if __name__ == '__main__':
    TicketBookingSystem().start()







           


        





