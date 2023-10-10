def fachrial(n):
      if n < 0:
       return 0
      elif (n == 0) or (n == 1):
        return 1
      else:
         fact=1
         while(n>1):
          fact=fact*n
          n=n-1
          return fact
print ("Enter a number ")          
num=int(input("num"))
print ("the fachrial of",num,"is =")
s=fachrial(num)
print(s)