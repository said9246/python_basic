# ------------data types in python----------------
a=10
b=20.5
c=5+6j
d="Hello"
e=True
f=None
g=[1,2,3,4,5]
h=(1,2,3,4,5)
i={1,2,3,4,5}
j={"name":"John", "age":30}
k=range(5)
l=bytes(5)
m=bytearray(5)
n=memoryview(bytes(5))
print(a,b,c,d,e,f)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))                      

print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))

# --- IGNORE ---  ~
#input

print("Welcome to the program!")
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name)
print("You are", age, "years old")
a=int(name)
b=int(age)

print(a + b)

print("Goodbye!")
print("Python", "is", "awesome", sep="-")
print("Hello", end=" ")
print("World!")

#type conversion

list1 = [1, 2, 3]
tuple1 = tuple(list1)
set1 = set(list1)

print(tuple1)
print(set1)

string = "Python"
print(list(string))
