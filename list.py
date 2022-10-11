def jam (a):
    b=[]
    for i in a:
        if i < 5:
            b.append(i)
    return b
if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print (jam(a))
    