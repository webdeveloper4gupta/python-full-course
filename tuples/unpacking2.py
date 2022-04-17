a=(1,2,3,4,5)
# a,b,c=a#it gives error
a,b,*c=a
print(a,b,c)