n = int(input("enter number:\n"))
if n%2 == 0:
  print("Pair")
elif n%2!=0 and n%3==0:
  print("Impair mais multipe de 3")
elif n%2!=0 and n%3!=0:
  print("Ni pair ni multiple de 3")
  
