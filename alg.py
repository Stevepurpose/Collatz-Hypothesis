c0 =int(input("Enter a non_negative integer here: "))

while c0!=1:
  
    if c0%2==0:
        c0=c0//2
        print(c0)

    elif c0%2==1:
      c0  = c0 * 3 + 1
      print(c0)

else:
    print("Exiting at 1")
    exit(0)
   