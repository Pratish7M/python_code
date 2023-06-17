# string
#upper to lower
#replace
#string[10]

str1 = "this is my first string"
print(type(str1))
print(str1)

'''multiple string'''
str2 = '''first line
second line
third line'''
print(str2)

'''string are arrays'''
string  = "hello pratish gurav"
print(string[6])

'''to get the length of string use len'''
length = len(string)
print(length)


'''check any word present in string or not'''

print("pratish" in string)
#output: true
print("yash" in string)
#output: false

if "pratish" in string :
    print("pratish present in string")
else :
    print("not present")

print("pratish" not in string)
# output : false

print("yash" not in string)
#output: true


'''convert capital letters to lower letter
you cant change orignal string letters format'''

string.upper()
print(string)
# output : hello pratish gurav

print(string.upper())
# output : HELLO PRATISH GURAV


'''REPLACING STRING 
in string we cant make changes in orignal string '''

replace = string.replace('pratish','yash')
print(replace)


