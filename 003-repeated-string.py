def repeatedString(s, n):
    # getting the quotient
    quotient = n // len(s)
    # find how many a's initially
    original_result = s.count('a')
    # get approximate result we get
    part_one = quotient * original_result
    # rest of 'a' which is not included in part one calc
    # basically get how many a's would be there when cutting before index
    part_two = s[:n%(len(s))].count('a')
    # return the sum of part one and two. Voila!
    return part_one + part_two
    

s = "aaaa"
n = 10

print(repeatedString(s, n))