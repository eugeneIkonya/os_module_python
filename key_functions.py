import os

#the function gives the name of th os dependent module
print (os.name)

#os.getcwd() -returns the current working directory
def get_dir():
    cwd=os.getcwd()
    print(cwd)

#os.open()-open a file
file_name="demo.txt"
new_file_name="new file.txt"
desktop_path="/Users/eugeneikonya/Desktop"


#to write a file
def write_file():
    file=open(file_name,'w')
    file.write("Hello OS module")
    file.close()

#to read from the file
def read_file():
    file=open(file_name,'r')
    text=file.read()
    print(text)

#to rename a file
def rename_file():
    file_name="old.txt"
    os.rename(file_name,'new.txt')


#os.access(path,mode)-to test if a file is accessible
#Modes are:
            # 1.os.F_OK-Found
            # 2.os.R_OK-readable
            # 3.os.W_OK-writable
            # 4.os.X_OK-executable
def check_access():
    print("For the file " + file_name + " Found, Readable, Writable, Executable :")
    #check if found
    is_found=os.access(file_name,os.F_OK)
    print(is_found)
    #check if readable
    is_readable=os.access(file_name,os.R_OK)
    print(is_readable)
    #check if writable
    is_writable=os.access(file_name,os.W_OK)
    print(is_writable)
    #check if executable
    is_executable=os.access(file_name,os.X_OK)
    print(is_executable)

#to change directories
def change_directory():
    os.chdir(desktop_path)
    get_dir()

def list_dir():
    path=os.getcwd()
    directories=os.listdir(path)
    for file in directories:
        print(file)

def make_dir():
    os.mkdir(new_file_name)
    list_dir()

def remove_dir():
    os.rmdir(new_file_name)
    list_dir()

make_dir()
remove_dir()


    






