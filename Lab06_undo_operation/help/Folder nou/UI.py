from PersonService import *
from ActivityService import*
class Console:
    def __init__(self,serv,act_serv):
        self._service=serv
        self._act_service=act_serv
        
    def printMenu(self):
        print("FOR PEOPLE:")
        print("     1. Add a person.")
        print("     2. Remove a person by ID.")
        print("     3. Update a person by ID.")
        print("     4. Show people.")
        print("FOR ACTIVITIES:")
        print("     5. Add an activity.")
        print("     6. Remove an activity.")
        print("     7. Update an activity by ID.")
        print("     8. Show activities.")
        print("9.Exit")
    
    def run (self):
        commands={'1':self.add_person,
                  '2':self.remove_person,
                  '3':self.update_person,
                  '4':self.show_people,
                  '5':self.add_activity,
                  '6':self.remove_activity,
                  '7':self.update_activity,
                  '8':self.show_activities}
        while True:
            self.printMenu()
            command=input("Enter command:")
            if command=='9':
                break
            elif command in commands:
                try:
                    commands[command]()
                except ValueError as e:
                    print(e)
            else:
                print("Bad command!")

    def add_person(self):
        personID=input("Enter an ID: ")
        name=input("Enter a name: ")
        phoneNo=input("Enter a phone number: ")
        try:
            self._service.add_person(personID,name,phoneNo)
        except Exception as error:
            print(error)
        
    def show_people(self):
        result=self._service.get_all()
        for i in result:
            print(i)
        
    def remove_person(self):
        personID=input("Enter the ID: ")
        try:
            self._service.remove_by_id(personID)
        except Exception as error:
            print(error)

    def update_person(self):
        personID=input("Enter the ID of the person you want to update: ")
        new_name=input("Enter a new name: ")
        new_phoneNo=input("Enter a new phone number: ")
        try:
            self._service.update_person(personID,new_name,new_phoneNo)
        except Exception as error:
            print(error)

    
    def show_activities(self):
        result=self._act_service.get_all()
        for i in result:
            print(i)

    def add_activity(self):
        activityID=input("Enter an ID: ")
        list_of_personIDs=[]
        print("Enter stop to stop reading person IDs.")
        personID=0
        while not personID=='stop':
            personID=input("Enter a person's ID: ")
            list_of_personIDs.append(personID)
        del list_of_personIDs[-1]
        date=input("Enter a date in format dd.mm.yyyy : ")
        time=input("Enter the time in format hh:mm : ")
        description=input("Enter a description: ")
        try:
            self._act_service.add_activity(activityID,list_of_personIDs,date,time,description)
        except Exception as error:
            print(error)

    def remove_activity(self):
        activityID=input("Enter the ID: ")
        try:
            self._act_service.remove_by_id(activityID)
        except Exception as error:
            print(error)

    def update_activity(self):
        activityID=input("Enter the ID: ")
        new_list_of_personIDs=[]
        print("Enter stop to stop reading the new person IDs.")
        personID=0
        while not personID=='stop':
            personID=input("Enter a person's ID: ")
            new_list_of_personIDs.append(personID)
        del new_list_of_personIDs[-1]
        new_date=input("Enter a new date in format dd.mm.yyyy : ")
        new_time=input("Enter the new time in format hh:mm : ")
        new_description=input("Enter a new description: ")
        try:
            self._act_service.update_activity(activityID,new_list_of_personIDs,new_date,new_time,new_description)
        except Exception as error:
            print(error)






serv=PService()
act_serv=AService(serv)
c=Console(serv,act_serv)
c.run()
