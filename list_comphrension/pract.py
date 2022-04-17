# here i have to ad only even index element of list1 to list2
list1=[1,2,3,4,5,6,7,8]
list2=[i1 for i,i1 in enumerate(list1) if i%2==0 ]
print(list2)