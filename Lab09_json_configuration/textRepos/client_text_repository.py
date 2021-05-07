'''
    CLIENT TEXT REPOSITORY
'''

from Repository import Repository
from domain import Client

class ClientTextRepository(Repository):
    def __init__(self, file_name):
        Repository.__init__(self)
        self._file_name = file_name
        self._load_file()
        self._save_file()


    def str_to_client(self, string):
        '''
        transforms a string into an object of type client
        params:
            string - (type string) a line in the file
        '''
        string = string.split(',')
        string[1] = string[1].replace('\n','')
        client = Client(int(string[0]),string[1])
        return client

    def client_to_str(self, client):
        return str(client.id) + ',' + client.name

    def add(self, element):
        '''
            adds an element to the repo and saves in the file
            params:
                element - will be added to self._repo (type list)
        '''
        self._repo.append(element)
        self._save_file()

    def delete(self, element_id):
        '''
            deletes an element from the repo and saves the file
            params:
                element_id - the id of the element (type int) 
        '''
        self._repo.remove(self.find(element_id))
        self._save_file()

    def update(self, client_id, new_name):
        '''
        updates a client
        params:
            client_id - (type int)
            new_name - (type str)
        '''
        k = self.find(client_id)
        k.name = new_name
        self._save_file()

    def _load_file(self):
        '''
            adds to the repository every client present in file
        '''
        f = open(self._file_name, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            client = self.str_to_client(line)
            self._repo.append(client)
        f.close()

    def _save_file(self):
        '''
            adds from repository to the file
        '''
        f = open(self._file_name, 'w')
        for client in self._repo:
            f.write(self.client_to_str(client))
            f.write('\n')
        f.close()