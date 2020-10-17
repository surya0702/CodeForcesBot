def menu():
    """
     Available options in the Bot
    """
    print()
    print("This BOT can do the following tasks:")
    print("1 . Available Tags")
    print("2 . Get programs based on Tags")
    print("3 . End this chat")
    print("------------------------------------")

    try:
        return int(input("Enter you choice [1-3] : ")) # Asks the User for choose the options
    except:
        print("PLEASE ENTER THE CHOICE IN THE GIVEN RANGE") # Throws an error if the input is not in the given range