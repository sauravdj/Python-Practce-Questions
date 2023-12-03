import sys
from encryption import loadPasswordFile, savePasswordFile , passwordEncrypt

#The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]

#The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

#The encryption key for the caesar cypher
encryptionKey = 16

while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print()
    choice = input("Please enter a number (1-6)")

    if(choice == '1'): #Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)
        

    elif(choice == '2'): #Lookup at password
        print()
        for keyvalue in passwords:
            print(keyvalue[0])
        passwordToLookup = input("Which website do you want to lookup the password for?")

        for i in range(len(passwords)):
            if passwords[i][0] == passwordToLookup:
                decryptedPassword = passwordEncrypt(passwords[i][1], -encryptionKey)
                print(" Decrypted password:", decryptedPassword)
                break
        #You will need to find the password that matches the website
        #You will then need to decrypt the password

        

    elif(choice == '3'):
        print()
        website = input("What website is this password for?")
        print()
        unencryptedPassword = input("What is the password?")

        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)

        password_entry = [website, encryptedPassword]
        passwords.append(password_entry)

        print("Password encrypted and saved.")

        print("Passwords List:", passwords)

    elif(choice == '4'): #Save the passwords to a file
            savePasswordFile(passwords,passwordFileName)
            print("Password file saved")


    elif(choice == '5'): #print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    elif(choice == '6'):  #quit our program
        sys.exit()
    else:
        print("Invalid choice. ")

    print()
    print()

