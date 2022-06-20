import os
import sys
import random

'''
When importing a file the code looks for the file within a list of directories (sys.path)
sys.path is a list of directories where the interpreter searches for the file
For example:
when importing os module the interpreter searches for the file in the following directories:
['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/majed/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
notice that the first directory is the current directory
which means that if we have a file name os.py within our directory then the interpreter will choose it over the original os module
avoid using common names like os, sys, math, random, etc. when naming your python files
'''

run_os_commands = False

if run_os_commands:
    try:
        os.listdir() # => by default returns a list of files in the current directory, but we can also specify a path(absolute or relative) //ls -a
        os.listdir('../') # => returns a list of files in the parent directory //ls -a ../
        os.listdir('/mnt/c/Users/MAJED/OneDrive/Desktop/upskilling-python') # => returns a list of files in the specified path //ls -a /mnt/c/Users/MAJED/OneDrive/Desktop/upskilling-python
        os.getcwd() #=> pwd


        #Run any os command using os.system(command)
        os.system('ls -a') #=> ls -a 

        os.remove('file.txt') #=> rm file.txt / for files only
        os.rmdir('folder') #=> rm -r folder / for direcotries only

        os.rename('file.txt', 'newfile.txt') #=> mv file.txt newfile.txt
        os.mkdir('newfolder') #=> mkdir newfolder



        os.path.exists('file.txt') #=> returns True if the file/directory exists
        os.path.isfile('file.txt') #=> returns True if the file exists as a file
        os.path.isdir('folder') #=> returns True if the directory exists as a directory

    except Exception as error:
        print(error)
        

#Random module
x = random.randint(1,10) #=> returns a random integer between 1 and 10(Exclusive)
print(x)

options = ['a', 'b', 'c']
x = random.choice(options) #=> returns a random element from the list

        




coin = ['H', 'T']
results = []

for i in range(1000000):
    results.append(random.choice(coin))

print("Heads: ", results.count('H'))
print("Tails: ", results.count('T'))
print("Heads percentage",  round(results.count('H')/len(results)*100, 2))














results = []
alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''
Fill with the chance:
1% of the array with random alphabets
99% of the array with random numbers
'''


for i in range(1000):
    if random.randint(1,100) == 1:
        results.append(random.choice(alphas))
    else:
        results.append(str(random.randint(1,500)))
        

# print(results)
    

    
    
'''
In Linux terminal we have 3 main files/streams:
1. stdin: input from the user (Linux  file_no: 0)
2. stdout: output to the user (Linux file_no: 1) => Default output
3. stderr: output to the user if there is an error (Linux file_no: 2)
'''


'''
Redirecting the output in linux terminal:
Syntax:
command file_no> file_name
if file_name is not specified then the output is redirected to the default output (stdout)
command > output.txt # Rerdirects the stdout to output.txt

For example for logging purposes:
we can redirect errors to log file to be revieed later

python3 file.py > output.txt 2> error.txt

'''
        
for number in results:
    if number.isnumeric():
        print(int(number))
    else:
        print(number, " Not a number", file=sys.stderr)
        
        
        


'''
Example:
let's say you have created a module called fff.py and you placed that in a directory called /home/majed/custom_modules.
By default the interpreter searches for the module in the directories found within the sys.path variable
to modify the sys.path variable we can use the following command:
import sys
sys.path.append('/home/majed/custom_modules')
import fff

'''