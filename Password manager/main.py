import random
import string

passwords = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8)) 
    return password
    
while True:
    print("\n------------Personal Password Manager------------------")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")
    
    choice= input("Enter your choice: ")
    
    
    if choice == "1":
        site = input("Enter website: ")
        pwd = input("Enter password: ")
        
        passwords[site]=pwd
        
        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
            
        print("Saved sucessfully")
        
        
    elif choice == "2":
        
        if not passwords:
            print("No data")
        else:
            for site,pwd in passwords.items():
                print(site,":",pwd)

    elif choice == "3":
        print("Generated Password", generate_password())
        
    elif choice == "4":
        print("Exiting.........")
        break
    else:
        print("Invalid choice")
