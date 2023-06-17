#default arguments
#keyword arguments
#required arguments
#varible length arguments

def name(fname = "pratish", mname = "chandu", lname= "gurav" ) :
    print("hello", fname,mname,lname)

name("yash") #mname and lname not difined so default values take
name(lname= "gurav", fname = "pratish", mname = "chandu") 
#sequence not required if values alreday given in def function

#varibble length arguments
def tup(*name):
    print(type(name))
    print("heyy", name[0],name[1],name[2])

tup("pratish","chandu", "khurdamoje")

def dec(**name):
    print(type(name))
    print("helli,", name["fname"], name["mname"], name["lname"])

dec(fname = "abhi", lname = "shaikh", mname = "bachhan")