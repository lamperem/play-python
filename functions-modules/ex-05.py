# Function as argument

def add(x, y):
	return x + y

def operation(func, x,y):
	return func(x,y)

x = 5
y = 10
result = operation(add,x,y)

print(result)