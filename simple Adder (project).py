try:
    print("Hello and Welcome to simple adder!😊")
    print("____________________________________")
    a = input("please enter the value of 'a':")
    b = input("please enter the value of 'b':")

    if a is not None and b is not None:
        try:
            print(f"the addition of a and b is {int(a) + int(b)}")
        except ValueError as e:
            print("you have entered invalid inputs \nplease enter a valid numeric value.🙄")

    print("_____________________________________")

except KeyboardInterrupt:
    print("\nbye bye.. 👋")