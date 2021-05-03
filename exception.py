while True:
    try:
        number = int(input("Enter a number"))
        print(18/number)
        break
    except ValueError:
        print("Make sure you enter an integer\n")
    except ZeroDivisionError:
        print("dont enter zero, u fool")
    finally:
        print("loop complete")




