a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
def main ():
    for i in a:
        if i < 5:
            b.extend ({i})
            
if __name__ == "__main__":
        main()
print (b)