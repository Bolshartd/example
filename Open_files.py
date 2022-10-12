def file():
    try:
        data = open('data.txt', 'r')
        data1 = data.read()
        return (data1.replace(",", " "))
    finally:
        data.close() 
if __name__ == "__main__":
    print (file())
