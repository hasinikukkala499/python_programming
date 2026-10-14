#contact managemet system
cbook={}
while(True):
    print("Welcome to contact management system")
    print("choose from the following options")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Display Contact")
    print("6.EXIT")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter ur name")
        phone=int(input("enter your phone no."))
        cbook[name]=phone
        print("added successfully")
    elif choice==2:
        name=input("enter the phone to be searched")
        if name in cbook:
            print("found",cbook[name])
        else:   
            print("not found")
    elif choice==3:
        name=input("enter the name for which value is to be updated")
        phone=int(input("enter new phone no."))
        if name in cbook:
            cbook[name]=phone
            print("updated")
        else:
             print("not found")
    elif choice==4:
        name=input("enter the name to be deleted")
        if name in cbook:
            del cbook[name]
            print("deleted successfully")
        else:                                                                      
            print("not found")
    elif choice==5:
        for key,value in cbook.items():
            print(key,value)
    elif choice==6:
        print("existing...Thankyou")
    else:
        print("invalid choice")
                                                    
                  
        
