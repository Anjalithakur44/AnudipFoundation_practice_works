#displaying a list
#complete list with formatting
list=[20,70,69,'hello',50]
print("List is :\n",list)
#only printing list elements without formatting
print(*list)
#accessing members using for loop
print("Elements using for loop")
for x in list:
    print(x, end=" ")

#fetching 3rd element
print("\n3rd element : ", list[2])
#fetching 4th elemt from last
print("4th element from last :", list[-4])
#fetching elements from 3rd position to 10th position
print("Elements from 3rd position to 10th position:", list[2:10])
#alternate elements from 3rd position to 10th position
print("Alternate elements from 3rd position to 10th position:", list[2:10:2])
#create a list of 20 numbers and print them in backward direction using forward index
mylist=[12,40,28,45,89,45,67,8,934,24,897,345,786,23,57,1,2,3,4,5]
x= len(mylist)-1
for index in range(x,-1,-1):
    print(mylist[index], end=" ")

#list creation
mylist2=[20,30,40,50]
x=int(input("\nEnter any number"))
mylist2.append(x)
print(mylist2)
second=[1,2,3,4]
mylist2.append(second)
print(mylist2)

#using extend
third=[5,6,7,8]
mylist2.extend(third)
print(mylist2)

#inserting element at specified position
mylist2.insert(5,147)
print(mylist2)

#find a method to insert all the elements of another sequence datatype at particular index in the list but all the elements must be inserted one by one
my_list = [1, 2, 3, 4, 5]
elements = [10, 20, 30]
index = 2

# Manually track the index for insertion
check = 0
for element in elements:
    my_list.insert(index + check, element)
    check += 1
    print(my_list)

#to delete last element
mylist.pop()
print(mylist)
#to delete second element
mylist.pop(1)
print(mylist)
#to delete  23
mylist.remove(23)
print(mylist)




