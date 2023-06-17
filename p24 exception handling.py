a = input("eneter the number : ")
x = [100,200]

try:
    print(f"{x[int(a)]}")
except ValueError :
    print("value error")
except IndexError :
    print("IndexError")
