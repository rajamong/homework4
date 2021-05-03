# creates a class called average
class average:
    # creates an empty constructor
    def __init__(self):
        pass

     # calculates the average of elements in a list
    def findmean(self, numlist):
        if (len(numlist) == 0):
            print('the list you entered is empty')
        else:
            return sum(numlist) / len(numlist)

# creates an empty list
#numlist = []
  
# asks user for number of elements in their list
#n = int(input("enter number of elements: "))
  
# iterating till all elements are stored
#for i in range(0, n):
    #elements = int(input())
    # adds the element to the list
    #numlist.append(elements) 

#print(numlist)
#print(findmean(numlist))
