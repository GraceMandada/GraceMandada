#function to return frequency of each word
def count_frequency(mylist):
    #create a dict object
    counts = {}

    #iterate the list
    for i in range(0, len(mylist)):
        
        #check if the word is there in the list
        if mylist[i] in counts.keys():
            
            #increment the count
            counts[mylist[i]] += 1
        
        else:
            #set the count to 1
            counts[mylist[i]] = 1
    
    #return the dictionary
    return counts


#call the count_frequency function
print(count_frequency(["one", "two", "eleven", "three", "one", "two", "eleven", "three", "seven", "eleven"]))