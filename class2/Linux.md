### Linux command structure:
* command/script options arguments
* Eg (mkdir -p 1/2/3/4/5):
    * command: mkdir
    * options: -p, --parents
    * args: 1/2/3/4/5

* For each commands you can check:
    * the help menu using --help option
    * Manual: man command_name


### Changing directory (cd)
* cd folderName
* cd foldername1/foldername2
* cd .. # going back a directory
* cd ../.. # Going 2 directories back

### type of paths
* Absolute path: /mnt/c/Users/MAJED/OneDrive/Desktop/upskilling-python
    *   starts with /

* Relative path:
    * in relation with your current location
    * Eg:
        *   starting from:  /mnt/c/Users/MAJED/OneDrive
        *   relative path of upskilling-python is Desktop/upskilling-python
    * Eg2:
        * starting from: /mnt/c/Users/MAJED/OneDrive/Desktop/ARC.Connect
        * relative path of upskilling-python: ../upskilling-python/


### Make direcrtory (mkdir)
* mkdir test
* important option:
    * -p:
        * parents
* cd  # back to your home directory (Default path)
* cd - # back to the previous directory

```
    mkdir practice
    test:
        newfolder
                test1
                test2
        newfolder2
                test1
        

```

### Option 1:
```bash
    cd /tmp
    mkdir testing
    cd testing
    mkdir newfolder
    mkdir newfolder2
    cd newfolder
    mkdir test1 test2
    cd ../
    cd newfolder2
    mkdir test1

```


### Option 2:

```bash
    mkdir /tmp/test
    cd /tmp/test
    mkdir newfolder newfolder2
    mkdir newfolder/test1 newfolder/test2
    mkdir newfolder2/test1

```

### Option 3:

```bash
    mkdir -p /tmp/test/newfolder/test1 /tmp/test/newfolder/test2 /tmp/test/newfolder2/test1
```


### List (ls)
* ls # shows file/directories in current directory
* ls folder # listing files in folder
* ls -l  # lists files / one file per line.
* ls -a # shows files starting with '.' (hidden files/directories)
* ls -h # show human readable units(file size) best used with -l

### Print working directory (pwd)
* Print the absolute path for your current working directory.


### cat 
* cat Linux.md # shows you the file's content
* cat -n numbers all output lines.


### less
* simillar to cat.
* used to load bigger files.
* it doesn't load the entire file. Instead it devides the file into chunck and load them into your RAM.
* use Q to quit less.

### Defining a varialble in Linux
* x='test'
* x="test"
* x=test
* x=5
* Dont' leave space before or after the equal sign.

### echo
* echo hello
* echo $hello
* echo $x
* echo x

### history
* shows you commands history
* history -c #this command clears your history


### file
* shows you the file type.

### touch
* Used to create files.
* touch file1
* touch file1 file2 file3

### remove (rm) 
* used to remove file/directories.
* rm fileName
* rm file1 file2
* rm -r folder1 # used to delete directories.

### copy (cp)
* used to copy files/directories
* cp filename newName
* cp filename /tmp
* cp filename /tmp/newName
* cp -r folder /tmp


### move (mv):
* used to rename files
* used to move files
* mv fileone newname
* mv fileone /tmp
* mv directory newName
* mv directory /tmp

### clear:
* it clears your terminal.
* or use: CTRL + L