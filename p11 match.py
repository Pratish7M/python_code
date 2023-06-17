x = int(input("enter thr number : "))

match x :
   case 0 :
      print("xis zero")
   case 1 :
    print("x is one")
   case _ if x < 100 :
    print("x is less than zero")
   case _ if x == 90 :
    print("x is 90")
    
   case _ :
    print("x")
