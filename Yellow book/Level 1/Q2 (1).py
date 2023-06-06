def __main__():
  nums=[5,85,0,7,4,8,4,9,97,76,5,8]
  listlen=len(nums)
  for i in range(0,listlen):
    print(nums[i]+nums[i-1])

__main__()