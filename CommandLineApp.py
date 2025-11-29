def Palindrome():
    x = input("Enter an input: ")
    result = (x == x[::-1])
    print(result)
    return result

def Lower():
    x = input("Enter an input: ")
    result = x.islower()
    print(result)
    return result

def Digit():
    x = input("Enter an input: ")
    result = x.isdigit()
    print(result)
    return result

def Long():
    x = input("Enter an input: ")
    result = len(x) > 15
    print(result)
    return result

def Empty():
    x = input("Enter input: ")
    result = (x == "")
    print(result)
    return result

def Exit():
    print("Exit successfully")

def ChooseOperation(choice):
    match choice:
        case "1":
            Palindrome()
        case "2":
            Lower()
        case "3":
            Digit()
        case "4":
            Long()
        case "5":
            Empty()
        case "6":
            Exit()
        case _:
            print("Invalid choice")

while True:
    print("The available operations are:")
    print("1 - Palindrome: Check if the input is palindrome")
    print("2 - Lower: check if all characters in the input are lowercase")
    print("3 - Digit:  check if all characters in the input are digits")
    print("4 - Long: check if the input length is longer than 15")
    print("5 - Empty: check if the input is empty")
    print("6 - Exit")
    choice = input("Please enter the number of the operation you choose: ")
    ChooseOperation(choice)
    if choice == "6":
        break
