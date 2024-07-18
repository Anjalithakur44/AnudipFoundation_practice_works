list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("3rd element",list[2])
print("4th element",list[3])
print("Alternate from 3 to 10",*list[2:10:2])
# print number in backward direction using forward keyword
print("numbers are=")
n=len(list)-1
for i in range(n,-1,-1):
    print(list[i],end=',')
# inserting element at end oflist
x=int(input("\nEnter any number="))
y=int(input("\nEnter any number="))
list.append(x)
list.append(y)
print(list)
z=[1,2,3,4,5,6,7,8,9,10,11,12]
list.extend(z)
print(list)
list.insert(4,147)
print(list)