import os
def dir():
    this_dir = os.getcwd()
    return(os.listdir(this_dir))
if __name__ == "__main__":
    print(dir())