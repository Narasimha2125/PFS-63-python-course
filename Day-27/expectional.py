try:
    a = int(input())
except ValueError:
    print("Enter the correct datatype")
else:
    print("a=",a)
finally:
    print("End of the program")

try: 
    a = int(input("Enter the number: "))
    k = {1: 12, 12: 13}
    l = [232, 54]
except ValueError:
    print('Enter the correct datatype: ')
except KeyError:
    print('Key is not there')
except IndexError:
    print('Index out of range')
except ZeroDivisionError:
    print('Cant divide with zero')
except TypeError:
    print('Enter the correct datatype: ')
except NameError:
    print('Define the variable')
else:
    print("a: ", a)
finally:
    print("Execution completed!!")

try: 
    a = int(input("Enter the number: "))
    k = {1: 12, 12: 13}
    l = [232, 54]
except( ValueError,KeyError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")

try: 
    a = int(input("Enter the number: "))
    k = {1: 12, 12: 13}
    l = [232, 54]
    print(1[10])
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")


try: 
    amount = int(input("enter the amount: "))
    balance = 5000
    if amount < 0:
        raise Exception("Amount needs to be positive")

    
except Exception as e:
    print("Error occured:",e)
else:
    print("Error free program")
finally:
    print("End of the program")