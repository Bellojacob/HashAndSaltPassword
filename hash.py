
import re
# This program will accept user input and return a hash of the user's input

def hash():
    print("Please input a password that contains: atleast 8 characters(maximum of 14), 1 numbers, and 1 special character")
    
    while True:
        userInput = input("Enter a Password: ")
        if len(userInput) < 8:
            print("Too Short! Password must be at least 8 characters long and less than 14 characters")
        elif len(userInput) > 14:
            print("Too long! Password must be at least 8 characters long and less than 14 characters")
        elif not re.search(r'\d', userInput):
            print("Password must contain at least 1 number.")
        elif not re.search(r'[!@#$%^&*()\-_=+{};:,<.>/?\|`~\[\]]', userInput):
            print("Password must contain at least 1 special character.")
        else:
            print("Password accepted.")
            break
    
    
    charArray = []
    for x in userInput:
        charArray.append(x)
    
    charArray.sort()
    print(charArray)
    
    #create new array
    
    hashedArray = []
    for y in charArray:
        hexValue = hex(ord(y))
        hashedArray.append(hexValue)
        
    hashedPassword = ""
    for z in hashedArray:
        hashedPassword += z
    
    
    print(hashedPassword)
    
    return hashedPassword
hashedPassword = hash()

def addSalt(hashedPassword):
    print("This is the hashed password: " + hashedPassword)
    print(len(hashedPassword))
    
    AmountOfSaltNeeded = 64 - len(hashedPassword)
    print(AmountOfSaltNeeded)
    
    # for the amount of salt needed, generate characters
    saltArray = []
    while AmountOfSaltNeeded != 0:
        SaltCharIndex = int(AmountOfSaltNeeded / 2 + 3)
        if SaltCharIndex < len(hashedPassword):  # Ensure the index is within the bounds
            SaltChar = hashedPassword[SaltCharIndex]
            saltArray.append(SaltChar)
            AmountOfSaltNeeded -= 1
        else:
            break  # Stop the loop if the index is out of bounds
    
    print(saltArray)
    
    for z in saltArray:
        hashedPassword += z
        
    print(hashedPassword)
    # should be 64 every time
    print(len(hashedPassword))

addSalt(hashedPassword)