# code keys: def(function), if elif else, for while, class
# pass 
# is_hungry = True False  uppercase
# print(type(3.24))
# print(type(new_person))
# print(len(new_person))
# print(len("coding dojo"))
# cast >> num to str >> print("hello"+ str(42))
# upside down >> from str to int >> total = 34, user_val ="26" >> total = total+ int(user_val)
# total = total + int("26")
# for x in range(0,10,1):

print("Hello World!")

x = "Hello Python"
print (x)

y = 42
print (y)

print("this is a sample string")

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is" + name)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name}{last_name} and I am {age} years old.")


first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and i am {} years old".format(first_name, last_name, age) )

j = "hello world"
print(j.title())
print(j.upper())
print(j.lower())
print(j.count())
print(j.split())
print(j.find())
print(j.isalnum())
print(j.isalpha())
print(j.isdigit())
print(j.islower())
print(j.isupper())
print(j.join())
print(j.endswith())


def add(a,b):
    x =a+b
    return x
sum1 = add(4,6) >>10
sum2 = add(1,4) >>5
sum3 = sum1 + sum2 >>15
