print("\n 1st code")
x = "pratish"
for i in x :
    print(i)


print("\n 2nd code")
x = "pratish"
for i in x :
    print(i)
    if i== "s" :
      break 


print("\n 3rd code")
x = ["red","blue","green"]
for colour in x :
    print(colour)
    for i in colour :
        print(i)
    
        
print("print table of 5")
for i in range(12) :
    if (i == 11) :
     break
    print("5 * ",i,"=",5*i)
''' output : 
5 *  0 = 0
5 *  1 = 5
5 *  2 = 10
5 *  3 = 15
5 *  4 = 20
5 *  5 = 25
5 *  6 = 30
5 *  7 = 35
5 *  8 = 40
5 *  9 = 45
5 *  10 = 50
'''


print("print table of 5")
for i in range(13) :
    if (i == 11) :
     continue
    print("5 * ",i,"=",5*i)
    
''' output : 
5 *  0 = 0
5 *  1 = 5
5 *  2 = 10
5 *  3 = 15
5 *  4 = 20
5 *  5 = 25
5 *  6 = 30
5 *  7 = 35
5 *  8 = 40
5 *  9 = 45
5 *  10 = 50
5 *  12 = 60'''


