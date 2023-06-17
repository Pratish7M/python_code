#slicing
#striping
#counting
#find

string = "hello pratish gurav"

print(string[0:13])
#output : hello pratish

print(string[-1])
#output : v

print(string[0:-1])
#output :hello pratish gura

print(string[0:19])
#output :hello pratish gurav

print(string[-5:-1])
#output : gura

'''The strip() method removes any whitespace from the beginning or the end:'''
string2 = "  hello  "
print(string2)
print(string2.strip())

'''count'''
n = string.count("pratish")
print(n)
#output : 1

'''find'''
x = string.find("prati")
print(x)