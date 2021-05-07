class User():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday #ddmmyyyy

        #extract first and last names
        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]


user1 = User("Calvin Klein","01041977")

user1.age = 50
print(user1.name, user1.birthday)
print(user1.first_name)
print(user1.last_name)