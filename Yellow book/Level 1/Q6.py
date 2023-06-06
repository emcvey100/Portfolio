import numpy
def __main__():
  nums=[5,85,0,7,4,8,4,9,97,76,5,8]
  for i in nums:
    calc = numpy.mod(i,5)
    if calc ==0 and i !=0:
      print(i)
__main__()