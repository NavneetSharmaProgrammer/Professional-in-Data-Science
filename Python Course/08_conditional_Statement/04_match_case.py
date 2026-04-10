a = int(input("Enter a lucky number between 1 and 10: "))

match a:
    case 1:
        print("You have won a car!")
    case 3:
        print("You have won a bike!")
    case 6:
        print("You have won a watch!")
    case _:
        print("Better luck next time")