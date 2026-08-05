#a = 1

#while a<= 30:
#   print(a)
#    a = a+1

#a = int(input("tell your number:"))
#while a >0:
 #   print(a%10)
  #  a = a//10

#a = int(input("tell your number:"))
#
#rev = 0
#
#while a >0:
#    rev = rev*10 +a%10
#    #print(a%10)
#    a = a//10
#print(rev)
#

a = int(input("tell your number:"))

copy = a
rev = 0

while a >0:
    rev = rev*10 +a%10
    #print(a%10)
    a = a//10
if copy==rev:
    print("palindrom number")
else:
    print("not a palindrome number")        

