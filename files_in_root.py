def dir():
    import os
    this_os = os.getcwd()
    return(os.listdir(this_os))
if __name__ == "__main__":
    print(dir())