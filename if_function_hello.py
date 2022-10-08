def your_name():
    name = input("Write your name:")
    if name == ("Artem"):
        print ("Hello Artem!")
    else:
        print ("Try again")
        return your_name()
your_name()