def countingValleys(steps, path):
    # first create variables for altitude and valleys
    altitude = 0
    valleys = 0
    # now create simple loop
    for step in path:
        # check if letter is U or climbing
        if step == "U":
            # if that's the case, is it below altitude
            # meaning that is equal to -1
            if (altitude == -1):
                # then we have a valley
                valleys +=1
            # and increase the altitude
            # so we can sure it is a valley
            altitude +=1
        # no check if it is "D" or descending
        if step == "D":
            # then decrease the altitude
            altitude -=1
    # and return the valleys! Voila!
    return valleys




steps = 8
path = "UDDDUDUU"

print(countingValleys(steps, path))