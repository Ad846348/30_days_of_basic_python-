import json

contacts = {}

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except:
        contacts = {}

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f)

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    save_contacts()
    print("Contact saved ✅")

def show_contacts():
    if len(contacts) == 0:
        print("No contacts")
    else:
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def search_contact():
    name = input("Enter the name : ")
    print(contacts.get(name, "No contact found"))

load_contacts()
while True:
    print("\n1.Add 2.Show 3.Search 4.Exit")
    ch = input("Choice: ")
    if ch == '1': add_contact()
    elif ch == '2': show_contacts()
    elif ch == '3': search_contact()
    elif ch == '4': break