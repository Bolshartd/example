def file():
    with open('data.txt') as data:
        data1 = data.read()
        return (data1.replace(",", " "))
if __name__ == "__main__":
    print (file())
