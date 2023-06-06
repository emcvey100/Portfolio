def printing(words):
  def size(string):
    length=0
    for i in string:
      if length<len(i):
        length=len(i)
    return length

  frame=lambda leng: "*"*(leng+2)

  def frames(passage,big):
    while len(passage)<big:
        passage+=" "
    line="*" + passage + "*"
    return line
  num=size(words)
  print(frame(num))
  for i in words:
    print(frames(i,num))
  print(frame(num))

words=input("Passage:").split()
printing(words)

