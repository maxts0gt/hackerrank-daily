# Hackerrank No.001: Sock Merchant

def sockMerchant(n, ar):
    # first create dictionary to track pairs
    numberOfPair = {}
    # create variable to count the number of pairs
    result = 0
    # create simple loop
    for number in ar:
        # check if the number is in the dictionary
        if number in numberOfPair:
            # if so, add 1 to it
            numberOfPair[number] += 1
        else: 
            # if it doesn't exist, then assign 1
            numberOfPair[number] = 1
        # now we check if it is pair or not by dividing 2
        if numberOfPair[number] % 2 == 0:
            # if it is, then increase the result
            result+=1
    # and finally return the result. Voila
    return result




exampleArray = [10, 20, 20, 10, 30]
n = 9

print(sockMerchant(n, exampleArray))