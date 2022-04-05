# Leetcode No11: Container with most water

def maxArea(height):
    # record the max area
    result = 0
    # create two pointers
    left = 0
    right = len(height) - 1
    # create loop where while left < right -> Loop!
    while (left < right):
        # update max area with previous max area and 
        # min of both sides * right - left
        # this means basically find out the area (height * width)
        result = max(result, min(height[left], height[right])*[right-left])
        # then check if left side is lower than right
        if (height[left] < height[right]):
            # if so, move left by + 1
            left += 1
            # else move right by - 1
        else:
            right -= 1
            # and return the result. Voila!
    
    return result

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
