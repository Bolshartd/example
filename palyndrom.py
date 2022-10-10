def word():
    if x == r:
        return("palyndrom", x)
    else:
        return("not palyndrom", x)
        
if __name__ == "__main__":
    x = "wow"
    r = "".join(reversed(x))
    print(word())