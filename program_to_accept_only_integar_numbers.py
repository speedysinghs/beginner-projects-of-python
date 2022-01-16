list = []
while(True):
    try:
        num = input("Enter any integar value or q to quit: ")
        if num != "q":
            list.append(int(num))  #   this will throws a valueError if "num" is a character value thus this will
                                    #  go in 'except' 
        elif num == "q":
            break

        
    except ValueError:
        print("Error: Please put integar only")
 

print(list)