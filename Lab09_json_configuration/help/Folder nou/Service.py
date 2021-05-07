from PersonRepository import*
import random
class Service:
    def __init__(self):
        self._repo=PRepo()
        self.init_list_of_people()

    def init_list_of_people(self):
        list_of_first_names=['Ion','Maria','Olga','Lenuta','Mihai','Diana','Viorica','Constantin','Carmen','Alex','Dan','Stefan Jr']
        list_of_last_names=['Popescu','Enescu','Vasile','Vasilica','Lazar','Dumitrescu','Manole','Daesei','Ionescu','Ungureanu']
        list_of_ids=range(1000,9999)
        list_of_phoneNo=range(1000000,9999999)
        for i in range(10):
            choosed_id=str(random.choice(list_of_ids))
            choosed_first_name=random.choice(list_of_first_names)
            choosed_last_name=random.choice(list_of_last_names)
            choosed_name=choosed_first_name+' '+choosed_last_name
            choosed_phoneNo='07'+str(random.choice(list_of_phoneNo))
            person=Person(choosed_id,choosed_name,choosed_phoneNo)
            if self.validateID(choosed_id)=='valid':
                self._repo.add(person)
            else:
                i=i-1 

    def validateID(self,personID):
        result=self._repo.find_by_id(personID)
        if result!=None:
            return 'invalid'
        return 'valid'

    def validate_name(self,value):
        if value==None:
            raise BadNameError("Bad name!")
        for i in value:
            if not(i>='a' and i<='z' or i>='A' and i<='Z' or i==' '):
                raise BadNameError("Bad name!")
        return None

    def validate_phoneNo(self,phoneNo):
        if phoneNo.isdigit()==False:
            raise BadPhoneNo("Bad phone number!")
        return None   

    def add_person(self,personID,name,phoneNo):
        if self.validateID(personID)=='invalid':
            raise BadIDError("This ID already exists!")
        if self.validate_name(name)==None and self.validate_phoneNo(phoneNo)==None:
            person=Person(personID,name,phoneNo)
            self._repo.add(person)
    
    def get_all(self):
        return self._repo.get_all()

    def remove_by_id(self,personID):
        element=self._repo.find_by_id(personID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of people!")
        self._repo.remove(element)

    def update_person(self,personID,new_name,new_phoneNo):
        element=self._repo.find_by_id(personID)
        if element==None:
            raise NonExistentID("This ID does not exist in the list of people!")
        if self.validate_name(new_name)==None and self.validate_phoneNo(new_phoneNo)==None:
            new_person=Person(personID,new_name,new_phoneNo)
            self._repo.update(element,new_person)



