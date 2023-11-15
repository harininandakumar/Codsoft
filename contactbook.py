contact={}


def display_contact():
    print("name\t\tcontact number\t\taddress")
    for key in contact:
        print("{}\t\t{}\t\t{}".format(key,contact.get(key)))
while True:
    choice=int(input("1.new contact \n 2.search contact \n 3.display \n 4.exit"))
    if choice==1:
        name=input("enter contact name:")
        phone=input("mobile number:")
        address=input("enter the address:")
        contact[name]=phone,address
    elif choice==2:
        search_name=input("enter contact name")
        if search_name in contact:
            print(search_name,"s,contact number is",contact[search_name])
        else:
            print("name is not found in contact book")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("enter the contact to be edited")
        if edit_contact in contact:
            phone=input(" mobile number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("name is not found in contact book")
    elif choice==5:
        del_contact=input("enter the contact to be deleted")
        if del_contact in contact:
            confirmation=input("do you want to delet y/n")
            if confirmation=='y' or confirmation=='y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("name is not found in contact book")
    else:
        break

