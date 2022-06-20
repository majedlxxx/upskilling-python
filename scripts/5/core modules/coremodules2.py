# sys continued:
import sys


print(sys.argv)
#sys.argv is just a method to pass input/arguments to the program through the command line
# python3 coremodules2.py Majed 26
if len(sys.argv) < 2:
    print("Name is missing", file=sys.stderr)
    exit()
    
name = sys.argv[1]
print("Hello", name)

if len(sys.argv) < 3:
    print("Age is missing", file=sys.stderr)
    exit()

age = sys.argv[2]
if not age.isnumeric():
    print("Age is not a number", file=sys.stderr)
    exit()
    
age = int(age)
print("Your age is", age)

#Arguments vector:
'''
sys.argv[0] => script name
sys.argv[1] => first argument
sys.argv[2] => second argument
.
.etc
'''
