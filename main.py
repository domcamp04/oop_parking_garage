class ParkingGarage:
    open_spots = 25
    parked_cars = []
    current_ticket = []
    
    def __init__(self, open_spots, parked_cars, unpaid_ticekts):
        self.open_spots = open_spots
        self.parked_cars = parked_cars
        self.current_ticket = unpaid_ticekts
        
    def takeTicket(self): 
        if self.open_spots > 0:
            v_id = input("Enter license plate: ")
            self.parked_cars.append(v_id)
            self.current_ticket.append(v_id)
            self.open_spots -= 1
        else:
            print("No open spots, Sorry. ")    
        
    
    def payForParking(self):
        selection = input("Enter License Plate: ").lower()
        if selection in self.current_ticket:
            payment = input("Please enter 'pay' to pay for your ticket ").lower()
            if payment == 'pay': 
                self.current_ticket.remove(selection)
                print("Thank you, have a nice day")
            else:
                print("Pay to exit garage by entering 'pay' ")
        else:
            print("Invalid entry, please try again. ")

            
    def leaveGarage(self):
        exit = input("Please enter your license plate number: ")
        if exit not in self.parked_cars:
            print("That is not a valid license plate number, please try again.")  
        elif exit in self.current_ticket:
            print("Pay for parking before exiting ")
        elif exit in self.parked_cars and exit not in self.current_ticket:
            print("Thank you, have a nice day! ")
            self.open_spots += 1
            self.parked_cars.remove(exit)

    
def run():
    park = ParkingGarage
    while True:
        action = input("Please enter one of the following options: \n Enter 'take' to enter the garage \n Enter 'pay' to pay ticket \n Enter 'leave' to exit the garage ").lower()
        if action == "take":
            park.takeTicket(park)
        elif action == "pay":
            park.payForParking(park)   
        elif action == "leave":
            park.leaveGarage(park)
        else:
            print("Invalid entry.")
        
run()