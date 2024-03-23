def name():
    n = 1
    while n != 0:
        a = input("Enter your userID: ")
        b = input("Enter your password: ")
        if a == b:
            print("Successfully logged in")
            # Add a way to exit the loop
            break
        else:
            print('Reenter the details')
name()
