# try:
#     n = int(input("enter the index : "))
#     l = [1,2,3,4,5,6,7]
#     print(f"{l[n]}")
    


''' in this program we can see print(" i always execute ") its not 
    executed but if we use finally keyword then it will execute '''
def function():
    try:
        n = int(input("enter the index : "))
        l = [1,2,3,4,5,6,7]
        # print(f"{l[n]}")
        return l[n]
    
    except :
        print("error occured")
    
    # finally:
        print(" i always execute")

function()
# print(x)
    
