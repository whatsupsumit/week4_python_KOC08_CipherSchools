while True:
    try :
        number = int(input("enter a new number : "))
    except ValueError:
        print("Please type integer!! s")
    except:
        print("Unexpected error!!!")
    else:
        print(f'user input = {number}')
        break
    finally:
        print('finally blocks....')
        
        
    
    