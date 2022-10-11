def sort_dict(my_dict):
    for i in my_dict:
        return sorted(my_dict.values(), reverse = True)
if __name__ == "__main__":
    my_dict = {'a':500, 'c':560,'b':5874, 'd':400, 'e':5874, 'f':20}
    print(sort_dict(my_dict)[0:3])