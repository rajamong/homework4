# creates a class called cube
class cubevolume:
    # creates an empty constructor
    def __init__(self):
        pass

    # calculates the volume of a cube
    def volume(self, length): 
        if (type(length) is int):
            if (length > 0):
                return length * length * length
            else:
                print('the length you entered is invalid')
        
        else:
            print('the length you entered is invalid')

#while True:

    # take in the users input
    # length = float(input("pls enter your cubes length: "))
    
    # prints out the calculation
    # print("the volume of your cube is: ", volume(length))


