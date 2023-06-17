l = [7,8,9,5,4,6,3,1,2]

#sort
l.sort()
print(l)

l.sort(reverse=True)
print(l)

#index 
print(l.index(5))

#copy
m = l.copy()
m[0] = 100
print(m)

#insert
m.insert(1, 50)
print(m)


list = [i for i in range(45)]
print(list)

list1 = [i*i for i in range(10)]
print(list1)

list3 = [i+1*i+1 for i in range(10)]
print(list3)

list2 = [i for i in range(20) if i%2 == 0]
print(list2)