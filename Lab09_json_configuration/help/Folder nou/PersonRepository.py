from Person import*
class PRepo:
    def __init__(self):
        self._container=[]

    def validateID(self,personID):
        result=self.find_by_id(personID)
        if result!=None:
            return 'invalid'
        return 'valid'

    def add(self,element):
        self._container.append(element)

    def find_by_id(self,personID):
        for i in self._container:
            if i.personID==personID:
                return i
        return None

    def remove(self,element):
        self._container.remove(element)

    def get_all(self):
        return self._container

    def update(self,element,new_person):
        idx=self._container.index(element)
        self._container[idx]=new_person

    def no_of_people(self):
        return len(self._container)