## List( mutable, duplicates, Ordered, Heterogenous)
#
#a = [12,34,15,17,19]
#
## 1st way using index
#for i in range (len(a)):
#    print(a[i])
#
## 2nd way directly on values
#
#for i in a:
#    print(i)

#l = [ 1,2,3,4,5,6]
#l.append(7)
#l.insert(1,2)
#l.extend()
#l.remove(2)

#print(l)

#l = [1,2,3,4,5]
#l[0] = 10
#print(l)

##1
#l = [-45,67,12,-56,45,-59]
#
#print("positive element are:")
#for i in l:
#    if i >= 0:
#        print(i)
#   # elif i<0:
#    #    print(i)   
#print("negitive element are:")
#for i in l:
#    if i < 0:
#        print(i)    

##2
#l = [12,44,66,77,99]
#sum = 0
#
#for i in l:
#    sum = sum + i
#
#print(sum/len(l))    

##3
#l = [12,44,45,12,55,85,88,4]
#largest = l[0]
#for i in range(len(l)):
#    if l[i] >largest:
#        largest = l[i]
#        index = i
#print(f"your largest number is {largest} at index {index}")
#

##4
#l = [12,45,65,35,62,63]
#largest = l[0]
#sec_largest =l[0]
#
#for i in l:
#    if i>largest:
#        sec_largest = sec_largest
#        largest = i
#    elif i>sec_largest:
#        sec_largest = i    
#print(sec_largest,largest)

## 5
#l  = [ 12,13,14,4,15,16]
#for i in range (len(l)-1):
#    if l[i] < l[i+1]:
#        continue
#    else :
#        print("your list is not sorted")
#        break
#else:
#    print("your list is sorted")

l = [23,54,77,88]
for i in l:
    if l>l:
        print("list is sorted")
    else:
        print(" list is not sorted")    