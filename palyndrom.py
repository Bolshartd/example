def word(x):
    r = "".join(reversed(x))
    if x == r:
        return("palyndrom", x)
    else:
        return("not palyndrom", x)
        
if __name__ == "__main__":
    x = "wow"
    print(word(x))
    
