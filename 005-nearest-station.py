def sum_of_distance(S, P):
    # create result to record sum of distance
    result = 0
    # create min variable to store minimum value
    inside_min = 0
    outside_min = 0
    # create simple loop for people
    for person in P:
        # create simple loop for stations
        for station in S:
            # grab the current absolute min value
            current_min = abs(station - person)
            # check if current value < min value
            if current_min < inside_min:
                # update the min value
                inside_min = current_min
                # stop current iteration
                pass

        if inside_min < outside_min:
            # update outside min
            outside_min = inside_min
            pass

            # if didn't break, then update the min
        # after every inside loop, update the result
        outside_min = inside_min
        result += outside_min

    # and return result after loops. Voila!
    return result

S = [37, 12]
P = [12, 37]

S1 = [51, 1, 35]
P1 = [10, 20, 30, 40 , 50]

print(sum_of_distance(S1, P1))

