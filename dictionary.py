def biggest1(my_dict):
    max_ind = list(my_dict)[0]
    max_value = list(my_dict.values())[0]
    for i in my_dict:
        if my_dict[i] > max_value:
            max_value = my_dict[i]
            max_ind = i
    return max_ind, max_value
if __name__ == "__main__":
    my_dict = {'a':500, 'c':560,'b':5874, 'd':400, 'e':5874, 'f':20}
    print(biggest1(my_dict))
    