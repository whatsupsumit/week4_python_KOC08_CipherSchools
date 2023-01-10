# makea fiunction divide
# divide (a,b)

# please divide (4,2)
# please divide (4,0)  # please don't divide by zero , Zero
# print divide ('4',2)  # please input numbers only


# solution :
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        #print('you cannot divide a number by zero')
        print(err)
    except TypeError as err:
        print("numbers must be int or floats")
    except:
        print("Unexpected error")

        
print(divide(10,0))