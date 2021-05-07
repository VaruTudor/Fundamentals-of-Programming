def printReposWithMessage(msg, clientRepo, carRepo, rentRepo):
    print("-"*15 + msg + "-"*15)
    if clientRepo != None:
        print("Clients:\n" + str(clientRepo))
    if carRepo != None:
        print("Books:\n" + str(carRepo))
    if rentRepo != None:
        print("Rentals:\n" + str(rentRepo))  