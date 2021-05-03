# creates a class called fullname
class fullname:
    # creates an empty constructor
    def __init__(self):
        pass

    # combines the first name and last name
    def combine(self, firstname, lastname):
        if (firstname == ''):
            print('you are missing a first name')
        
        elif (lastname == ''):
            print('you are missing a last name')

        else:
            return firstname + " " + lastname

#while True:
    
    # take in the users inputs
    #firstname = str(input("pls enter your first name: "))
    #lastname = str(input("pls enter your last name: "))

    # prints out the combined name
    #print combine(firstname, lastname))
