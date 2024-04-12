# Case 1 - Method will not be overridden in class B and class C
# Case 2 - Method will be overridden in class B but not in class C
# Case 3 - Method will be overridden in class C but not in class B
# Case 4 - Method will be overridden in both class B and class C


class A:
    def method(self):
        print('This method belongs to class A')
    pass

class B(A):
    def method(self):
        print('This method belongs to class B')
    pass

class C(A):
    def method(self):
        print('This method belongs to class C')
    pass

class D(B, C):
    pass


d = D()
d.method() # This method belongs to class B