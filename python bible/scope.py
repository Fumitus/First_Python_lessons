a = [1,2,3] # global value

def f1():
    global a
    a[0] = 5 #global value
    print(a)

def f2():
    a = 50 #local value
    print(a)
f1()
f2()
print(a) #global value

# Two types of scope - Global & Local
# Python functions create local scopes
