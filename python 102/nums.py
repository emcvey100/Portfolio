def getNums(size):
    nums = []
    for x in range(size):
        num = int(input("Enter a whole number: "))
        nums.append(num)
    return nums


mynums = getNums(10)
