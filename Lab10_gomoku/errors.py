class WrongCoordinates(Exception):
    pass
    # def __str__(self):
    #     return 'You should have given 2 coordinates'
    # def __repr__(self):
    #     return 'You should have given 2 coordinates'
    
class OutsideBoard(Exception):
    pass
class Overwrite(Exception):
    pass