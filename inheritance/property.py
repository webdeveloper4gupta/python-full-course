# property attribute is used for treating any function as the datamember
class aman:
    a=90
    @property
    def sukri(self):#also know as getter
        return self.a+34

a=aman()
print(a.sukri)