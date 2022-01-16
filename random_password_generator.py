import random
letters = "abcdefghijklmnopqrstwuxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*123456798"
while True:
    password_len = int(input("Enter the password length: "))
    password_count = int(input("How many passwords would you like : "))
    for i in range(password_count):
        password = ""
        for j in range(password_len):
            password = password + random.choice(letters)
            
        print(f"Here's your password number {i+1} : {password}")
    break
