import sys
import os



FilePath=r"E:\PROJECTS\Note_taking_app" # takes raw string
UserFilePath=r"E:\PROJECTS\Note_taking_app\user_info.txt"

def star(func):
    def wrapper():
        print("*"*40)
        func()
        print("*"*40)
    return wrapper
    
@star
def title():
    print("Application to Record All Your Notes")

@star
def ending():
    print("""Thank You for using My Application
        Have a Nice Day
          """)

def decision():
    while True:
        
        ans=input("\nEnter y if you want to continue else n for exiting application: ").lower()
        if ans=="y":
            
            break
        elif ans=="n":
            sys.exit(0)
        else:
            os.system('cls')
            print("\nWrong option try again: ")

def register(username,password):
    with open(UserFilePath,"r") as f:
        users= f.read()
        users=users.strip()
        #print (users)
    if username in users:
        print("\nUser already Exist:")
        
    else:
        with open(UserFilePath,"a") as f:
            f.write(username + " : "+ password+"\n")
        print("\n Successfully Registered")
                
    
    
def dict_data(filename):
    dic={}
    with open(filename,'r') as f:
        for line in f:
            part= line.strip().split(':')
            if len(part)==2:
                key,value=part
                key,value=line.strip().split(':')
                dic[key.strip()] = value.strip()
    return dic
            
        
def create_file(FilePath,Filename):
    extension_File=(Filename+".txt")
    if os.path.isfile(os.path.join(FilePath,username,extension_File))!=True:
        with open(os.path.join(FilePath,username,extension_File),'w'):
            pass
    else:
        print("\nFile already exist: ")
            
                
def read_file(FilePath,Filename):
    extension_File=(Filename+".txt")
    if os.path.isfile(os.path.join(FilePath,username,extension_File))==True:
        with open(os.path.join(FilePath,username,extension_File),'r') as f:
            content=f.read()
        print("\n",content)
    else:
        print("\nFile does not exist: ")
            
    
def write_file(FilePath,Filename):
     extension_File=(Filename+".txt")
     content=input("\nEnter the content you wanna write in a file: ")
     if os.path.isfile(os.path.join(FilePath,username,extension_File))==True:
         with open(os.path.join(FilePath,username,extension_File),'a') as f:
            f.write("\n"+content)
     else:
         print("\nFile does not exist")
    
    
def view_file():
    files=os.listdir(os.path.join(FilePath,username))
    j=1
    for file in files:
        print(f"List of file in {username} folder are as follow:\n ")
        print(f"{j}. {file}\n")
        j+=1
def delete_file(FilePath,Filename):
    extension_File=(Filename+".txt")
    File=os.path.join(FilePath,username,extension_File)
    if os.path.isfile(File)==True:
        decision1=input("\nDo you really want to delete this file:(press either y or n): ").lower()
        while decision1 not in ["y","n"]:
            decision1=input("\nDo you really want to delete this file:(press either y or n): ").lower()
        if decision1=="y":
            os.remove(File)
        elif decision1=="n":
            print("Deletion cancelled: ")            
        
    else:
        print("\nFile does not exist: ")

def create_folder():
    dir=os.path.join(FilePath,username)
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    
def login(username,password):
    
    data=dict_data(UserFilePath)
    while True:
        try:
            
            
            if username in data and data[username]==password:
                create_folder()
                os.system('cls')
                title()
                print("HI, ",username,"\n")
                choice=int(input("""Enter your choice:
                         1. Press 1 for creating file
                         2. press 2 to read file
                         3. press 3 to write file
                         4. Press 4 to remove file
                         5. Press 5 to view your files
                         6. Press 6 to Logout
                         7. Press 7 to exit system
                         
                         Type Here: """))
                if choice== 1:
                
                    os.system('cls')
                    title()
                    print("HI, ",username,"\n")
                    Filename=input("Enter the name of file you want to create : ")
                    create_file(FilePath,Filename)
                    decision()
                elif choice==2:
                    os.system('cls')
                    title()
                    print("HI, ",username,"\n")
                    Filename=input("\nEnter the name of file: ")
                    read_file(FilePath,Filename)
                    decision()
                
                elif choice ==3:
                    os.system('cls')
                    title()
                    print("HI, ",username,"\n")
                    Filename=input("\nEnter the name of file u wanna write in : ")
                    write_file(FilePath,Filename)
                    decision()
                
            
                elif choice ==4:
                    os.system('cls')
                    title()
                    print("HI, ",username,"\n")
                    Filename=input("Enter the file you want to remove: ")
                    delete_file(FilePath,Filename)
                    decision()
            
                elif choice ==5:
                    os.system('cls')
                    title()
                    print("HI, ",username,"\n")
                    view_file()
                    decision()
                elif choice ==6:
                    os.system('cls')
                    break
                elif choice==7:
                    os.system('cls')
                    ending()
                    sys.exit(0)
                else:
                    os.system('cls')
                    title()
                    print("Wrong choice...Try again: ")
                    
            else:
                print("\nInvalid username or password.....try again:\n ")
                break
            
        except ValueError:
            title()
            print("\nEnter number from 1-6: ")
        except Exception as e:
            title()
            print("\nError has ocurred", e)
   

while True:
    try:
        title()
        #os.system('cls')
        choice=int(input("""Enter a choice:
                1. Press 1 to Register
                2. Press 2 to Login
                3. Press 3 to Exit
                
                Type Here: """))
        
        if choice==1:
            os.system("cls")
            title()
            username=input("Enter a User Name: ")
            password=input("\nEnter a Password ")
            register(username,password)
            decision()
            os.system('cls')
        elif choice==2:
            os.system('cls')
            title()
            username=input("\nEnter your username: ")
            password=input("\nEnter your password: ")
            os.system('cls')
            
            login(username,password)
            
            
            # os.system('cls')
            
        elif choice==3:
            os.system('cls')
            ending()
            sys.exit(0)
        else:
            os.system('cls')
            title()
            print("Wrong option...try again:\n ")
    
    except ValueError:
        title()
        print("Enter number from 1-3")
    
    
    except Exception as e:
        title()
        print("Error has occurred ",e)