a=90
def aman():
    # a=8#this is local varaible
    global a
    a=8
    print(a)

aman()
print(a)#here also value of a is change