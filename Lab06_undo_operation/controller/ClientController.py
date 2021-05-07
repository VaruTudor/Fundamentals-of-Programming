from domain import Client
from controller.undoController import FunctionCall, Operation

class ClientController:
    def __init__(self, undoController, rentalController, clientRepository):
        self._clients = clientRepository
        self._rentalController = rentalController
        self._undoController = undoController

    def add_client(self, client_id, name):
        client = Client(client_id, name)
        self._clients.add(client)

        undo = FunctionCall(self.remove_client, client_id)
        redo = FunctionCall(self.add_client, client_id, name)
        op = Operation(undo,redo)
        self._undoController.recordOperation(op)
        return client

    def remove_client(self, client_id):
        '''
            1. delete the client
        '''
        client = self._clients.find(client_id)
        print(client)
        self._clients.delete(client_id)
        print(client)
        undo = FunctionCall(self.add_client, client.id, client.name)
        redo = FunctionCall(self.remove_client, client_id)

        op = Operation(undo, redo)
        self._undoController.recordOperation(op)
        '''
            2. delete their rentals
        '''
        rentals = self._rentalController.filterRentals(client, None)
        for rent in rentals:
            self._rentalController.delete_rental(rent.id, False)
        return client

    def update_client(self, client_id, new_name):
        self._clients.update(client_id, new_name)

    def count_clients(self):
        return len(self._clients)

    def list_clients(self):
        '''
        prints the list of clients
        '''
        for i in self._clients._repo:
            print (i)

    def search_client_id(self, client_id):
        for i in self._clients._repo:
            if i.id == client_id:
                print (i)
    
    def string_matching(self, s1, s2):
        '''
        checks if s1 is a substring of s2
        params:
            s1 - (str)
            s2 - (str)
        output:
            True - s1 is a substring of s2
            False - s1 is not a substring of s2
        '''
        l1 = []
        l2 = []
        for i in s1:
            l1.append(i)
        for i in s2:
            l2.append(i)
        for i in range(len(s1)):
            if l1[i] != l2[i]:
                return False
        return True
        
    def search_client_name(self, name):
        for i in self._clients._repo:
            if self.string_matching(name, i.name):
                print (i)
    