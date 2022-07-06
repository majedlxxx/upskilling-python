
from xxlimited import new


def crstrip(string,char=" "):
    new_string = string
    while new_string[-1] == char:
        new_string = new_string[:-1] # cna be replaced with new_string.pop()
    return new_string
    
def clstrip(string, char=" "):
    new_string = string
    while new_string[0] == char:
        new_string = new_string[1:]
        
    return new_string


def cstrip(string, char=" "):
    new_string = crstrip(string, char)
    new_string = clstrip(new_string, char)
    return new_string

x = '    test s   '
print(x)
results = crstrip(x, ' ')
print(results+"***")
results = clstrip(x, ' ')
print(results + "***")
results = cstrip(x, " ")
print(results + "**")
x = 1
x = 5
x = 2.2
x = "data"

# what's different in python that the same variable can hold data of multiple types. That's mainly because whenever we assign new data to x. x is being destroyed and created again.

x = 1
x += 5 # x = x + 5
x -= 1
x *= 2
x /= 3

x = "test"
print(0, x[0]) #t
print(1, x[1]) #e
print(-1, x[-1])
print(-2, x[-2])


print(x, 5, 5+2, "test", 5==7)

x += " another test" #addition
print(x)

x = "test " * 5
print(x)

#string slicing
print(x[0:2]) #2 is not included

#x[start(zero):end(len(x)):step(default value = 1)]
print(x[0:3:2])

#remove last character 
x = x[0:-1] # removed space / last char
print(x)
print(x[5:0:-1])
print(x)
print(x[::-1]) #reverse x

#strip functions will not modify the original x
x.strip(" ") #remove left and write spaces
x.rstrip("\n") # remove \n from the end of the string
x.lstrip("\n") # remove \n from the beginning of the string
x = "-this is a test- --"
x.strip('-')
print(x) # x will not be changed

y = x.strip("-")
print("Unchanged x: ", x)
print("Y(stripped x): ",y)


words = x.split(" ") #get back of list consisting of the words in the string x. based in on space split
print(words)


words = ["aa", "bb", "cc"]
results = " ".join(words)
print(results)