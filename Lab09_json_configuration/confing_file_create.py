from configparser import ConfigParser

config = ConfigParser()

config['binary'] = {
    'clients' : "'clients.pickle'",
    'books' : "'books.pickle'",
    'rentals' : "'rentals.pickle'"
}

config['text'] = {
    'clients' : "'clients.txt'",
    'books' : "'books.txt'",
    'rentals' : "'rentals.txt'"
}

config['in-app'] = {
    'clients' : '',
    'books' : '',
    'rentals' : ''
}

config['json'] = {
    'clients' : "'clientsJSON.txt'",
    'books' : "'booksJSON.txt'",
    'rentals' : "'rentalsJSON.txt'"
}

config['lab'] = {
    'clients' : '',
    'books' : "'book2.txt'",
    'rentals' : ''
}

f = open('settings.properties', 'w')
config.write(f)