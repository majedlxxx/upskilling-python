from mathops.numops import add, multiply
from mathops.listops import sum_list

print('''Enter:
      1. Add two numbers
      2. Multiply two numbers
      3. add a list of numbers
      ''')

choice = int(input("Enter choice(1/2/3):"))
if choice in (1,2):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if choice == 1:
        print(num1,"+",num2,"=",add(num1,num2))
    if choice == 2:
        print(num1,"*",num2,"=",multiply(num1,num2))
        
if choice == 3:
    l = []
    n = int(input("Enter number of elements in the list: "))
    for i in range(n):
        l.append(int(input("Enter element: ")))
        
    print("Sum of the list is: ",sum_list(l))
        
