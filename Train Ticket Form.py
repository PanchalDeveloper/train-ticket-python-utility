#     stations = ["Raipur", "Durg", "Bhatapara", "Bilaspur Jn", "Pendra Road", "Anuppur Jn", "Shahdol", "Umaria", "Jhansi", "Katni Murwara", "Sagour", "Nizamuddin"]

import random
import os
import gc

output_folder = "Tickets"

stations = ["Raipur", "Durg", "Bhatapara", "Bilaspur Jn", "Pendra Road", "Anuppur Jn", "Shahdol", "Umaria", "Jhansi", "Katni Murwara", "Sagour", "Nizamuddin"]

stationInfo = ""

for i, j in enumerate(stations):
    stationInfo += str(f"\t{j} : {i}\n")


class Train:
    company = "Indian Railways"

    def __init__(self, tname, tnumber, tseats, tfrom, tto, chargePerKM):
        self.tname = tname
        self.tnumber = tnumber
        self.tseats = tseats
        self.bookedSeats = 0
        self.tfrom = tfrom
        self.tto = tto
        self.chargePerKM = chargePerKM
        self.train_stations = ["Raipur", "Durg", "Bhatapara", "Bilaspur Jn", "Pendra Road", "Anuppur Jn", "Shahdol", "Umaria", "Jhansi", "Katni Murwara", "Sagour", "Nizamuddin"]

    @property
    def availSeats(self):
        return self.tseats - self.bookedSeats

    @property
    def tfullname(self):
        return self.tname + " - " + str(self.tnumber)

    def bookTicket(self):
        if self.availSeats > 0:
            # try:
            print("{:^75}".format(f"\n****Enter Station Details****\n{stationInfo}"))
            sFrom = int(input("From :"))
            sTo = int(input("To : "))
            try:
                stationFrom = stations[sFrom]
                stationTo = stations[sTo]
            except:
                print("Please Enter Valid Value")
                self.bookTicket()

            date = input("Date : ")
            print("\n")

            print("{:^75}".format("\n****Enter Person Details****\n"))
            personDetails = []

            def addPerson():
                name = input("\tEnter Name : ")
                age = int(input("\tEnter Age : "))
                personDetails.append({"Name": name.title(), "Age": age, })
                newTicket = input("\tWant to Add More Persons !? (Enter y/yes or no will be \"default\") : ")
                print("\n")
                pnr = random.randrange(1000000000, 9999999999)
                
                if not os.exists(output_folder):
                    os.mkdir(output_folder)
                
                with open(os.path.join(output_folder, "All Booked Tickets.txt"), "w") as newAllTckts:
                    newAllTckts.write("")
                    with open(os.path.join(output_folder, "All Booked Tickets.txt"), "at") as AllTckts:
                        with open(os.path.join(output_folder, "All Booked Tickets.txt"), "rt") as readAllTckt:
                            AllTckt = readAllTckt.read()

                        while (str(pnr) in AllTckt):
                            pnr = random.randrange(1000000000, 9999999999)

                        if (newTicket.casefold() == "y") or (newTicket.casefold() == "yes"):
                            addPerson()
                        else:
                            with open(os.path.join(output_folder, f"Ticket - {pnr}.txt"), "at") as ticket:
                                data = ""
                                for listKey in personDetails:
                                    for dictKey in listKey:
                                        data += (f"{dictKey} : {listKey[dictKey]}\n")
                                    data += "\n"

                                AllTckts.write(f"{str(pnr)}\n")
                                ticket.write(
                                    f"\t\t\t{self.tfullname}\n\tStation From : {stationFrom.title()} \t\t Station To : {stationTo.title()}\n\tDate : {date} \t\t PNR No. : {str(pnr)}\n\n{str(data)}")
                self.bookedSeats += 1
            addPerson()
            print("{:^75}".format(
                "\n****Your Ticket Was Successfully Boocked****\n"))
            # except:
            #     print("{:^75}".format("\n****Please Enter Valid Details****\n"))
        else:
            print("Sorry ! This Train is Full. Please Try Booking on Another Train. ")

    def __str__(self):
        return f"{self.tfullname}"

    def trainFullInfo(self):
        return f"Train Name : {self.tfullname} \nTotal Seats : {self.tseats} \nAvailable Seats : {self.availSeats}"


cgsk = Train("CG Sampark Kranti", 12823,
             500, "Durg", "H Nizamuddin", 0.281)
godwana = Train("Godwana SF EXP", 12409,
                572, "Durg", "H Nizamuddin", 0.273)
cgexp = Train("Chhattisgarh EXP", 182347,
              480, "Durg", "H Nizamuddin", 0.260)
samta = Train("Samta EXP", 12807, 350, "Durg", "H Nizamuddin", 0.275)

# print(cgsk.tname, cgsk.tnumber, cgsk.tseats,
#       cgsk.tfrom, cgsk.tto, cgsk.chargePerKM)
# print(cgsk)


trainsInfo = ""
trainIndex = 1
for obj in gc.get_objects():
    if isinstance(obj, Train):
        trainsInfo += f"\tTrain No. {trainIndex} = {obj}\n"
        obj.tindex = trainIndex
        trainIndex += 1


myTrain = int(input(
    f"Choose Trains From Below List :-\n{trainsInfo}\n\nEnter Train Code : "))
if type(myTrain) == int:
    for obj in gc.get_objects():
        if isinstance(obj, Train):
            if obj.tnumber == myTrain or obj.tindex == myTrain:
                print(f"Your Selected Train is : {obj.tfullname}")
                obj.bookTicket()
                print(f"Booked Seats : {obj.bookedSeats}")
                print(f"Total Seats : {obj.tseats}")
                print(f"Available Seats : {obj.availSeats}")
                

else:
    print("\t\t***Please Enter Valid Train Code\\Number***")
