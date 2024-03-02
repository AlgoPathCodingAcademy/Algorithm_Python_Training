#Local scope
#Enclosing scope
#Global Scope

#Local Scope
def my_function():
    a = 10
    print('Inside my_function a value is: ', a)


my_function()
#print('Outside my_function a value is: ', a) # Not accessible

#Enclosing scope
def outer_function():
    a = 20
    def inner_function():
        # This is a inner function
        print("still be able to access variable: ", a)
    inner_function()
    
outer_function()
#print('Outside my_function a value is: ', a) # Not accessible



#Is localVar is within the enclosing scope of function B ?
def functionB():
    anotherLocalVar = "I'm local to functionB"

def functionA():
    localVar = "I'm local to functionA"    
    functionB()  # calling functionB from within functionA

functionA()

#Global Scope
b = 10
def outer_function():
    def inner_function():
        # This is a inner function
        print("still be able to access variable: ", b)
    inner_function()

outer_function()
print('Outside my_function a value is: ', b) #Accessible


#When the same variable name appearing in Local Scope, Enclosed Scope and Global Scope
c = "global"
def outer_function():
    c = "enclosed"
    def inner_function():
        # This is a inner function
        c = "local"
        print("Inner function:", c)
    inner_function()
    print("Outer function:", c)

outer_function()
print("Global:", c)

#Global Keyword
x = 300

def myfunc():
  #global x
  x = 200

myfunc()

print(x)

#nonlocal keyword
def myfunc1():
  x = "John"
  def myfunc2():
    #nonlocal x
    #global x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

'''
#myfunc2() is not nested inside myfunc1(), so there is no enclosing scope for myfunc2(). 
#The nonlocal keyword is used to work with variables in an enclosing scope, 
#but since there's no enclosing scope for myfunc2(), the code raises a SyntaxError: no binding for nonlocal 'x' found.
def myfunc2():
    nonlocal x
    x = "hello"

def myfunc1():
  x = "John"
  myfunc2()
  return x

print(myfunc1())
'''
