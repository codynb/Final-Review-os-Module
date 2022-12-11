#Cody Brown, Exam 3 Review, OS module!

 #FILE NAMES AND PATHS
# Files are organized into directories, also called folders (for this example, the directory
# is OSrev), every running program has a 'current directory'
# the os module provides functions to work with files and directories
    # NOTE: os stands for 'operating system'

# Finding the current working directory
#--------
import os
cwd = os.getcwd()
    # cwd means current working directory
print(cwd)
    # this prints /Users/codybrown/Desktop/OSrev
    # this result is called a path
        # a file name, such as OSRv.py is considered a path, but it is relative

# Finding the absolute path
os.path.abspath('some.txt')
    # some.txt is an empty textfile in the OSRv folder
#--------

# ABOUT THE OS MODULE
#What exists?
#--------
os.mkdir()
    # this creates a directory named path with numeric module
    # mode
os.listdr()
    # returns a list of names of the entries in the directory given
    # by a path (arbitrary order)
os.rename()
    # renames a file or directory src to dst, if dst exists
    # will fail
    # AKA we a renaming the path and changing where it is
    # located
#--------

# CHANGING DIRECTORY
os.chdir('/Users/codybrown/Desktop/OSrev')
    # changing the current directory to what is said in the parenthesis
cwd = os.getcwd()
print(cwd)
print(os.listdir())
    # this prints:
        # /Users/codybrown/Desktop/OSrev
        # ['OSRv.py', 'some.txt']


# MAKING A NEW DIRECTORY
os.mkdir('Docs1')
    # this made a folder inside the OSrev folder called Docs1
print(os.listdir())
    # this printed ['OSRv.py', 'some.txt', 'Docs1'], notice the existence of 'Docs1'
    # which was not there until we just created it
os.rename('some.txt','Docs1/some.txt')
    # this moved some.txt into the Docs1 folder in OSrev
