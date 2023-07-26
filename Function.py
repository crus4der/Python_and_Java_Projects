print("\nExer 1")
def func(age, name):
    print(name + " "+ str(age) + " years old")

func(18, "Arsen")

print("\nExer 2")
def func2(*args):
    for i in args:
        print(i)

func2(20, 80, 60)
func2(20, 80, 60)

print("\nExer 3")
def calculation(a,b):
   a += 10
   b += 20
   return a, b

res = calculation(40, 10)
print(res)

print("\nExer 4")
def showEmployee(name, salary = 9000):
    print("Employee", name, "salary is:", salary)
showEmployee("ben ", 9000)
showEmployee("ben")

print("\nExer 5")
def funcx(a,b):
    def funcy(a, b):
        return a + b
    add = funcy(a, b)
    return add + 5
result = funcx(2, 10)
print(result)

print("\nExer6")
def recur(num):
    if num:
        return num + recur(num-1)
    else:
        return 0
result = recur(10)
print (result)

print("\nExer7")
def displayStudent(name, age):
    print(name, age)

displayStudent("Emma", 26)

def showStudent(name, age):
    return displayStudent(name, age)

showStudent("Emma", 26)

print("\nExer8")
print(list( range(4, 30, 2)))

print("\nExer")
aList = [4, 6, 8, 24, 12, 2]
print(max(aList))