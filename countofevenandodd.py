n=int(input("enter the number of terms:")) # taking value from user
l=[]  # empty list
even=0
odd=0
for i in range(n):  # states that taking values of that range
    s=int(input())
    l.append(s)
print(l)  # print list after adding elements

for i in l:   # checking for even numbers
    if i%2==0:
        even+=1
    else:     # checking for odd numbers
        odd+=1
print("total number of even numbers:",even)  # print count of even and odd numbers
print("total number of odd numbers:", odd)

output: [1,2,3,4,5,6,7,8,9]
       total number of even numbers: 4
       total numbe rof odd numbers: 5
