def arithmetic(x ,y, z):
        if z == "+":
                return (x+y)
        elif z == "-":
                return (x-y)
        elif z == "*":
                return (x*y)
        elif z == "/":
                return (x/y)
        else:
                return ("unknown operation")
def main():
        target = 1
        for i in range(1,11):
                print(f"{target}*{i} = {arithmetic(target, i,'*')}")
                        
if __name__ == "__main__":
        main()