def register():
    db = open("database.txt", "r")
    # users signup information
    Username = input("Create username:")
    password = input("Create password:")
    password1 = input("Confirm password:")
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    #confirm users password if they match
    if password != password1:
        print("password does not match, restart")
        register()
    # The password shouldnt be less than 7 characters    
    else:
        if len(password)<=7:
            print("password too short, restart:")
            register()
        elif Username in d:
            print("Username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write (Username+","+password+"\n")
            print("success!")



def access():
    db = open("database.txt","r")
    #users login information
    Username = input("Enter username:")
    password = input("Enter password:")

    if not len(Username or password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
           if data [Username]:
               try:
                   if password == data[Username]:
                      print("Login successfull")    
                      print("Hi,",Username)
                   else:
                        print("password or Username is incorrect")
               except:
                     print("incorrect password or username")
           else:
                print("Username or password doesn't exist")
        except:
            print("username or password doesn't exist")
    else:
        print("please enter a value")        

def home(option=None):
    option = input("Login | signup:")
    if option == "Login":
       access()
    elif option == "signup":
       register()
    else:
        print("please enter an option")
home()                           

                
    


