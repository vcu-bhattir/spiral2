def spiralize(size, n=1):
    
    squaresList = [i*i for i in range(1, size+1) if (i % 2 != 0)]
    nums = [i for i in range(1, size*size+1) if (i % 2 != 0)]

    index = 0
    b = 0
    return_value = 0

    for i in nums:

        return_value += nums[index]

        if (nums[index] == nums[len(nums)-1]):
            break

        if (nums[index] in squaresList):
            b += 1

        index += b 
        
    return return_value
