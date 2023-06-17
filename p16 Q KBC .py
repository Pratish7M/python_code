que = [1,2,3]
ans = ["a","b","d"]

# que[0] = "a"
# que[1] = "b"
# que[2] = "d"

# que[0] = "what is the capital of nepal"
# que[1] = "who is pratish's favorite"
# que[2] = "what's india cureent gdp"

# ans[0] = "a"
# ans[1] = "b"
# ans[2] = "d"/
balance = 0
# if True :
#   print('''what is the capital of nepal?
#   \n a.kathmandu
#   \n b.mumbai
#   \n c.delhi
#   \n d.tokyo''')
#   ans[0] = input("enter your answer : ")
# elif ans[0] == "a":
#   print("your anser is correct")
#   balance = balance + 10000
# else :
#   print("your anr is wrong")
  


if ans[0] == "a" :
 print('''who is pratish's favorite?
 \n a.sakshi
 \n b.jaya
 \n c.shradha
 \n d.aliya''')
 ans[1] = input("enter your answer : ")
 if ans[1] == "b" :
    balance = balance + 10000
    print("your answer is correct, you win : ",balance)
    if ans[1] == "b" and ans[0]== "a" :
     print('''what's india cureent gdp?
  \n a. 2.5 trillon $
  \n b. 1.97 trillion $
  \n c. 8.4 trillion $
  \n d. 3.83 trillion $''')
    ans[2] = input("enter your answer : ")
 elif ans[2] == "d" :
  balance = balance + 10000
  print("your answer is correct, you win : ",balance)
 elif ans[0] == "d" :
  print("your answer is wrong")
 else :
   print("your anr is wrong")

# if ans[1] == "b" and ans[0]== "a" :
#   print('''what's india cureent gdp?
#   \n a. 2.5 trillon $
#   \n b. 1.97 trillion $
#   \n c. 8.4 trillion $
#   \n d. 3.83 trillion $''')
#   ans[2] = input("enter your answer : ")
# elif ans[2] == "d" :
#  balance = balance + 10000
#  print("your answer is correct, you win : ",balance)
# elif ans[0] == "d" :
#  print("your answer is wrong")





