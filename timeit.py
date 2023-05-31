import random
s =[ ]
for f in range(1, 1000):
    s.append(random.randint(1, 300))

def small():
  n=400
  for i in s:
    if i<n:
      n=i
small()
def test():
    global s
    s.sort()
test()
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
