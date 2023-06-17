# 0,1,1,2,3,5,8
def fibo(n):
    f1 = 0
    f2 = 1
    
    for i in range(n) :
        fn = f1 + f2
        print(f1)
    
        f1 = f2
        f2 = fn
        

fibo(10)
print("hello")